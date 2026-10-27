from django.urls import path
from .views import recommend_box, recommend_box_for_order
urlpatterns = [
    path(
        "recommend/<int:product_id>/",
        recommend_box,
        name="recommend-box",
    ),
    path(
        "orders/<int:order_id>/recommend/",
        recommend_box_for_order,
        name="recommend_box_for_order",
    ),
]