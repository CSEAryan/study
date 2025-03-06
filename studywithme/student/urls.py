from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.student_login, name="login"),
    path("videos/", views.videos, name="videos"),
    path("logout/", views.logout, name="logout"),
]
