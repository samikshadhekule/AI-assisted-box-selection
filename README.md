AI-Assisted Box Selection System

--About the project--

I built this project using python and django to recommend a suitable shipping box for a product or order. The system schecks the product dimensions, weight and cost of available boxes before making a recommendation.I also used Django REST Framework to create APIs for getting box recommendations.

--Technologies used--
Python
Django
Django REST Frmework
SQLite Git and GitHub

--Features--
1. add products with their dimensions and weight.
2. add shipping boxes with their dimensions, weight capacity, and cost.
3. check whether a product fits inside a box, including when the product is rotated.
4. check whether the box can handle the required weight.
5. select the cheapest box that passes the implemented checks.
6. get box recommendations for products and orders through API endpoints.
7. test the selection logic using Django automated tests.

--How to run the project--

First, clone the repository and open the project folder in the terminal.
Create a virtual environment:
    Python -m venv myenv
Activate it on windows:
    myenv\Scripts\activate
Install the required packages:
    pip install django djangorestframework
Run the database migrations:
    python manage.py makemigrations 
    python maage.py migration 
Start the development server:
    python manage.py runserver

--API endpoints--
1. recommend a box for a product
GET/api/recommend/<product_id>/
2. recommend a box for an order
GET/api/orders/<order_id>/recommend/
Replace the ID with an existing product or order ID

--Running the tests--

run this command from the folder containning manage.py
    python manage.py test packaging

--Current limitations--
The system checks product dimensions individually and checks the total weight  of an order against the boxs weight capacity. However it does not guarantee that multiple products will physically fit together in the same box.

--AI usage--

I used ChatGPT for guidance while developing this project and understanding the code. The AI_USAGE.md file explains how i used AI and how i checked the code.