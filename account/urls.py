from django.urls import path

from . import views
from cinema.views import buy_ticket,movie_detail

urlpatterns = [
    path("login", views.login_request,name="login"),
    path("register", views.register_request,name="register"),
    path("loguot", views.logout_request,name="logout"),
    path("profile", views.profile_request,name="profile"),
    path('movie/<slug:slug>/buy/',buy_ticket, name='buy_ticket'),
    path('movie/<slug:slug>/', movie_detail, name='movie_detail'),
]
