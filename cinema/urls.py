from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('""', views.index, name='home' ),
    path('', views.movie_list, name='movie_list'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('buy-ticket/<slug:movie_slug>/', views.buy_ticket, name='buy_ticket'),
    path('ticket_list/', views.ticket_list, name='ticket_list'),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  \
 + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
