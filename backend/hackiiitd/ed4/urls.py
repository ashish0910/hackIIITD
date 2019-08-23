from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home', views.HomeView, name="home"),
    url(r'^testing', views.TestView, name="testing"),
    url(r'^generatetext', views.SaveTxtFile.as_view())
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)