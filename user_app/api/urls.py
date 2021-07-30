from django.urls import path, include
from rest_framework.authtoken import views
from .views import logout

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='api-login'),
    path('api-logout/', logout, name='api-logout'),
]