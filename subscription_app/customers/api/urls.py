from django.urls import include, path

from .views import ( 
    CustomerApiView,
    CustomerDetailView,
    # CustomerSubscriptionView
)

urlpatterns = [
    path('', CustomerApiView.as_view()),
    path('<int:customer_id>/', CustomerDetailView.as_view()),
    # path('<int:customer_id>/subscription', CustomerSubscriptionView.as_view()),
]