from django.urls import path

from .views import register, change_password

app_name = 'user_app'

urlpatterns = [
    path('register/', register, name='register'),
    path('change-password/', change_password, name='change-password'),
]