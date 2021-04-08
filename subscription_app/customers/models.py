from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postal_code: models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def post(self, request)
    #     return self.create(request)

class Subscription(models.Model):
    # One to one relationship w. Customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    plan_name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.plan_name

class Gift(models.Model):
    # Many to one relationship w. Customer gift_set
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    price: models.IntegerField()
    recipient_email = models.CharField(max_length=100)

    def __str__(self):
        return self.recipient_email
