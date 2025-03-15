from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('', views.users_main_view, name='user_main'),
    path('register/', views.user_registration_view, name="registration"),
    path('login/', views.user_login_view, name="login"),
    path('logout/', views.user_logout_view, name="logout")

]