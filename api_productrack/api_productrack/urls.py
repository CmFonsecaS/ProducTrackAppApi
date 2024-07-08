from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_productrack_app.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]