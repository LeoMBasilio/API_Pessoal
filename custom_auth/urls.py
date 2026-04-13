from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginViewSet, RegisterViewSet, UserViewSet, SuperuserViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'users', UserViewSet, basename='users')
router.register(r'superusers', SuperuserViewSet, basename='superusers')

urlpatterns = router.urls + [
    path('refresh/', TokenRefreshView.as_view()),
]