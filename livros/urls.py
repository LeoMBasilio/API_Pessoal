from rest_framework import routers
from .views import LivroViewSet

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livros')

urlpatterns = router.urls
