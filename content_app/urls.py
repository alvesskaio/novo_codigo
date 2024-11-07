from rest_framework.routers import DefaultRouter
from .views import MemberViewSet,ConviteViewSet,CadastroViewSet,SistemaViewSet

router = DefaultRouter()

router.register(r'member', MemberViewSet)
router.register(r'convite', ConviteViewSet)
router.register(r'cadastro', CadastroViewSet)
router.register(r'sistema', SistemaViewSet)

urlpatterns = router.urls