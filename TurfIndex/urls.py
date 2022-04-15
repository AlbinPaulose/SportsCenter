from django.urls import path, include
from . import views

urlpatterns = [
    path('turf_index', views.turf_index, name="turf_index"),
    path('turf_login', views.login_turf, name="turf_login"),
]