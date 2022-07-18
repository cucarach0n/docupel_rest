from rest_framework.routers import DefaultRouter
from apps.usuario.api.views.perfil_views import PerfilViewSet
router = DefaultRouter()

router.register(r'perfil',PerfilViewSet, basename = 'Perfil-view')
urlpatterns = router.urls