from apps.accesoTeam.api.views.permisosRol_views import *
from rest_framework.routers import DefaultRouter
from apps.accesoTeam.api.views.rol_views import *
router = DefaultRouter()

router.register(r'rol',RolTeamViewSet, basename = 'RolTeam-view')
router.register(r'permiso',PermisoRolViewSet, basename = 'PermisoRol-view')
urlpatterns = router.urls