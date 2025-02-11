from django.urls import path

from .views import register, change_password, user_settings, verify_code

app_name = 'user_app'

urlpatterns = [
    path('register/', register, name='register'),
    path('change-password/', change_password, name='change-password'),
    path('settings/', user_settings, name='user-settings'),
    path('verify-code/', verify_code, name='verify_code'),
]