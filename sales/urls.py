from django.urls import path

from sales import views

app_name = "sales"
urlpatterns = [
 
    path('sales_points_list/', views.sales_points_list, name='sales_points_list'),
    path('add_sales_point/', views.SalesPointsCreateView.as_view(), name='add_sales_point'),
    path('update_sales_point/<int:pk>', views.update_sales_point, name='update_sales_point'),
    path('delete_sales_point/<int:pk>', views.delete_sales_point, name='delete_sales_point'),


]
