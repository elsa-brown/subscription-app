from django.urls import include, path

from .views import ( CustomerViewSet )

urlpatterns = [
    path('', CustomerViewSet.as_view()),
]