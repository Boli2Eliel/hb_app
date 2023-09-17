from django.urls import path

from records import views

app_name = "records"
urlpatterns = [
    path('home/', views.home, name="home"),
    path('records/', views.records, name="records"),
    path('staff/', views.staff_list, name="staff"),

    path('products_list/', views.products_list, name="products_list"),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>', views.customer_product, name='product_details'),
    path('update_product/<int:pk>', views.update_product, name='update_product'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),

    path('formules_list/', views.formules_list, name="formules_list"),
    path('add_formule/', views.FormuleCreateView.as_view(), name='add_formule'),
    path('update_formule/<int:pk>', views.update_formule, name='update_formule'),
    path('delete_formule/<int:pk>', views.delete_formule, name='delete_formule'),

    path('uoms_list/', views.uom_list, name='uoms_list'),
    path('add_uom/', views.UomCreateView.as_view(), name='add_uom'),
    path('update_uom/<int:pk>', views.update_uom, name='update_uom'),
    path('delete_uom/<int:pk>', views.delete_uom, name='delete_uom')


]
