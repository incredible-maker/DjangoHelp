from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'about', views.about),
    path(r'articles/', include('articles.urls')),
    path(r'homepage', views.homepage),
    path(r'index', views.index),
    path(r'lifediary', views.lifediary),
]

urlpatterns += staticfiles_urlpatterns()
