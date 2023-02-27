from django.urls import path
from .views import register, EditProfilePageView, ShowProfilePageView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("<int:pk>/edit_profile", EditProfilePageView.as_view(), name="edit-profile"),
    path("<int:pk>/profile", ShowProfilePageView.as_view(), name="show-profile"),
    
    # path('password/', PasswordsChangeView.as_view(template_name = "registration/change_password.html"), name="change-password"),
    # path('password_success', views.password_success, name= "password_success"),
    
]