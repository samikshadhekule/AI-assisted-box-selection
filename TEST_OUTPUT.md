--Test command--
 python manage.py test packaging

 --Result--
 * total test cases:8
 ----------------------------------------------------------------------
Ran 8 tests in 0.019s

--Test cases covered
1. selects a suitable box for a product.
2. returns no  box when the product does not fit.
3. rejects boxes with insufficient weight capacity.
4. selects the cheapest suittable box.
5. selects a suitable  box for an order.
6. returns no bbox for an empty order.
7. rejects a box when the orrder weight exceeds its capacity.
8. checks order weight capacity when multiple units are ordered.