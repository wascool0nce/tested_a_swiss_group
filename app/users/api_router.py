from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
]

urlpatterns += router.urls


