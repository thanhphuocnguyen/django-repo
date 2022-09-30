from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from .views import ChangePassword, RegisterView, UpdateUserInfoView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='get_token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterView.as_view(), name='register'),
    path(
        'change-password/<int:pk>/',
        ChangePassword.as_view(),
        name='change_password',
    ),
    path(
        'update-profile/<int:pk>/',
        UpdateUserInfoView.as_view(),
        name='change_profile',
    )
]
