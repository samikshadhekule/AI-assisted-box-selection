from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .box_selector import  select_box
from .serializers import ShippingBoxSerializer
from .models import Order
from .box_selector import select_box_for_order

@api_view(["GET"])
def recommend_box(request, product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    box=select_box(product)

    if box is None:
        return Response(
            {"message" : "No suitable box found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer=ShippingBoxSerializer(box)
    return Response(serializer.data)

@api_view(["GET"])
def recommend_box_for_order(request, order_id):
    try:
        order=Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response(
            {"error" : "Order not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    box=select_box_for_order(order)

    if box is None:
        return Response(
            {"message":"No suitable box found for this order"},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer=ShippingBoxSerializer(box)
    return Response({
        "order_id":order.id,
        "recommended_box":serializer.data,
    })