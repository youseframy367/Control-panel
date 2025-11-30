from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('creatAcount/',views.creatAcount , name="creatAcount"),
    path(' /', views.add_supplier, name='Suppliers'),
        path('suppliers-json/', views.suppliers_json, name='suppliers_json'),
  path("orders/", views.orders_view, name="orders"),
    path("orders-json/", views.orders_json, name="orders_json"),
    path("manageStore/",views.manageStory ,name='manageStore'),
    path("Inventory/",views.Inventory ,name="Inventory"),
    path('dashbord/',views.dashbord ,name='dashbord'),
]


