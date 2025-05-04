from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/<str:type_user>", views.login, name="login"),
    path("admin/create_seller_login",
         views.create_seller_login, name="create_seller_login"),
    path("create_default_data", views.create_default_data,
         name="create_default_data")
]
