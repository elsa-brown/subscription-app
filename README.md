# subscription-app

A simple REST API for customers, subscriptions, and gifts, built with Python and Django. (work in progress)

### Setup
* Clone repo
* `pip install -r requirements.txt`
* `pip manage.py runserver`
* Visit `http://127.0.0.1:8000/customers/api/` to use API visual interface

### Usage
Add a new customer:
* Visit `http://127.0.0.1:8000/customers/api/`
* Add a customer's data in JSON format and click POST button
* Sample data set:
```
{
  "first_name": "Ernest",
  "last_name": "Hemingway",
  "address_1": "907 Whitehead St",
  "address_2": "",
  "city": "Key West",
  "state": "FL",
  "postal_code": "33043"
}
```
* Your first customer will be stored under the id `1`, and subsequent customers will be stored at the corresponding ascending index.
* You can view a customer's data by visiting `http://127.0.0.1:8000/customers/api/<customer_id>`. 
* For example, `http://127.0.0.1:8000/customers/api/1`.

### TODO
* When a customer is posted, return that customer data with their corresponding id.
* At `http://127.0.0.1:8000/customers/api/<customer_id>/subscription`, the user should be able to add subscriptions to the corresponding customer. This feature was blocked and left out due to time constraints.
* Add POST routing for gifts at `http://127.0.0.1:8000/customers/api/<customer_id>/gifts`
* Complete UPDATE and DELETE routes for customers, subscriptions, and gifts

### Notes on process
I used this excercise as an opportunity to learn Python and Django. I spent about 2 hours doing tutorials and installing python and django, then set up my project, and coded the models and initial views. Then I did some more learning about Django REST APIs and coded the API views until I got blocked and it was a good stopping point.
