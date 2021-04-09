from django.http import HttpRequest, HttpResponse

from .models import Customer, Subscription, Gift

def index(request):
    return HttpResponse("hello world")

def detail(request, customer_id):
    return HttpResponse("Information for Customer %s." %customer_id)

def subscription(request, customer_id):
    return HttpResponse("Subscriptions for Customer %s" %customer_id)

def gifts(request, customer_id):
    return HttpResponse("Gifts for Customer %s" %customer_id)
