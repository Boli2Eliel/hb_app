from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from authentication import views

urlpatterns = [
    # path('test/', views.test, name="test" ),
    path('', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path('accounts/', views.users_list, name="accounts"),
    path('user-update/<int:pk>', views.user_update, name='user-update'),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout")

]
