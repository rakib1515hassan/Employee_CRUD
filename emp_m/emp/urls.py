from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('base/',base, name="base"),
    path('add_emp/',add_emp, name="add_emp"),
    path('update_emp/',update_emp, name="update_emp"),
]