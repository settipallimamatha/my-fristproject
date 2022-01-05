from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from .views import StudentCurd, login

router = routers.DefaultRouter()
router.register(r'students', StudentCurd, basename="students")


urlpatterns = [
    path("",include(router.urls)),
    path('login/', login)
]
