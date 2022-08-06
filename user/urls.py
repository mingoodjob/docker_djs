from django.urls import path
from user import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('check/', views.UserCheckView.as_view()),
]
