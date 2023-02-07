from django.urls import path
from rest_framework.authtoken import views

from .views import (
    RegisterAPI,
    logout_user

)
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', logout_user, name='logout')
]
