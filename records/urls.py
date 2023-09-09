
from django.urls import path

from records import views

app_name = "records"
urlpatterns = [
    path('', views.home, name="home" ),
    path('products_list/', views.products_list, name="products_list" ),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>', views.customer_product, name='product_details'),

]
