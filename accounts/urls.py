from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('orders/', order_history, name='orders'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('logout/', user_logout, name='logout'),
    path('send_mail/', send_mail, name='send_mail'),
    path('signup_otp/', signup_otp, name='signup_otp'),
    path('register/', user_register, name='register'),
]
