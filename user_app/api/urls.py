from django.urls import path, include
from rest_framework.authtoken import views
from .views import logout, registration

# simple jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # token auth for mobile
    path('api-token-auth/', views.obtain_auth_token, name='api-login'),
    path('api-register/', registration, name='api-register'),
    path('api-logout/', logout, name='api-logout'),

    # jwt for javascript(Vue, React) etc
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]