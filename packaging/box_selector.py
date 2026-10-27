from . models import ShippingBox
from .models import Order
def dimensions_fits(product, box):

    product_dimensions = sorted([product.length, product.width, product.height,])
    box_dimensions = sorted([box.length, box.width, box.height,])
    return all(
        product_dim <= box_dim
        for product_dim, box_dim
        in zip(product_dimensions, box_dimensions)
    )

def select_box(product):
    boxes = ShippingBox.objects.all()
    suitable_boxes =[]

    for box in boxes:
        if dimensions_fits(product, box) and product.weight <= box.max_weight:
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda box: box.cost)
    return suitable_boxes[0]

def select_box_for_order(order):
    boxes=ShippingBox.objects.all()
    order_items=order.items.select_related("product").all()

    if not order_items.exists():
        return None

    total_weight=sum(
        (item.product.weight * item.quantity for item in order_items),
        start=0,
    )
    suitable_boxes=[]

    for box in boxes:
        if total_weight > box.max_weight:
            continue
        all_products_fit=all(
            dimensions_fits(item.product, box)
            for item in order_items
        )
        if all_products_fit:
            suitable_boxes.append(box)
    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda box: box.cost)
    return suitable_boxes[0]