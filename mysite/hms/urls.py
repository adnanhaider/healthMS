from django.urls import path
from hms import views

urlpatterns =[
    path('', views.health_check_view, name='health_check'),
]