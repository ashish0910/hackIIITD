from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', views.HomeView, name="home"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)