from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/<str:type_user>", views.login, name="login"),
    path("admin/create_seller_login",
         views.create_seller_login, name="create_seller_login"),
    path("create_default_data", views.create_default_data,
         name="create_default_data"),
    path("admin/get_seller", views.get_seller, name="get_seller"),
    path("admin/get_seller_login", views.get_seller_login, name="get_seller_login"),
    path("admin/get_client", views.get_client, name="get_client"),
    path("admin/get_product", views.get_product, name="get_product"),
    path("admin/get_production", views.get_production, name="get_production"),
    path("admin/get_orders", views.get_orders, name="get_orders"),
    path("admin/make_product", views.make_product, name="make_product"),
    path("admin/update_production/<str:code_product>",
         views.update_production, name="update_production"),
    path("admin/get_cant_product", views.get_cant_product, name="get_cant_product"),
    path("make_order", views.make_order, name="make_order"),
    path("create_client", views.create_client, name="create_client")
]
