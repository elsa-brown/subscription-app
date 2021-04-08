from django.urls import include, path

from .views import ( 
    CustomerApiView,
    CustomerDetailView
)

urlpatterns = [
    path('', CustomerApiView.as_view()),
    path('<int:customer_id>/', CustomerDetailView.as_view()),
]