
from django.urls import path

from records import views

app_name = "records"
urlpatterns = [
    path('', views.home, name="home" ),
    path('products_list/', views.products_list, name="products_list" ),

]
