from django.test import TestCase

# Create your tests here.
from decimal  import Decimal

from .models import Product, ShippingBox, Order,OrderItem
from .box_selector import select_box, select_box_for_order

class BoxSelectorTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )
        self.large_box=ShippingBox.objects.create(
            name="large box",
            length=35,
            width=25,
            height=15,
            max_weight=5,
            cost=25,
        )
    def test_selects_suitable_box(self):
        box=select_box(self.product)
        self.assertEqual(box, self.large_box)

    def test_returns_none_when_no_box_fits(self):
        self.product.length=100
        self.product.width=80
        self.product.height=75
        self.product.weight=20
        self.product.save()

        box=select_box(self.product)
        self.assertIsNone(box)

    def test_does_not_select_box_with_insufficient_weight_capacity(self):
        ShippingBox.objects.create(
            name="light box",
            length=35,
            width=25,
            height=15,
            max_weight=1,
            cost=5,
        )
        box=select_box(self.product)
        self.assertEqual(box, self.large_box)

    def test_selects_cheapest_suitable_box(self):
        cheaper_box=ShippingBox.objects.create(
            name="medium box",
            length=32,
            width=22,
            height=8,
            max_weight=3,
            cost=15,
        )
        box=select_box(self.product)
        self.assertEqual(box,cheaper_box)

    def test_selects_box_for_order(self):
        order=Order.objects.create()
        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=1,
        )

        box=select_box_for_order(order)

        self.assertEqual(box, self.large_box)

    def test_returns_none_for_empty_order(self):
        order=Order.objects.create()
        box=select_box_for_order(order)
        self.assertIsNone(box)

    def test_rejects_box_when_order_weight_exceeds_capacity(self):
        order=Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=3,
        )
        box=select_box_for_order(order)
        self.assertIsNone(box)

    def test_multiple_items_must_fit_order_weight_capacity(self):
        order=Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=3,
        )

        box=select_box_for_order(order)
        self.assertIsNone(box)