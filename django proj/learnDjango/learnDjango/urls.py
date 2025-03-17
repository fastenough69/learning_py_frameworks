"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
from hello import views

user_patt = [
    path("<str:name>", views.user),
    path("<str:name>/<int:age>", views.user),
]

products_patt = [path('', views.products), 
                 path("info", views.info_product),]


urlpatterns = [
    path("", views.index),
    re_path(r"^about", views.about),
    path('help', views.help),
    path("user", views.user),
    re_path("^user/", include(user_patt)),
    path("products/<int:id>/", include(products_patt)),
    path("new_user/", views.first_hendler),
    path("help_info", views.help_info),
    path("details", views.details),
    re_path("^worker", views.json_out),
    re_path("^set", views.set_cck),
    re_path("^get", views.get_cck),
]
