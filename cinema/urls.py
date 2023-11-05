from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home" ),
    path('movie/<slug:slug>/', views.movie_details, name='movie_details'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  \
 + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)