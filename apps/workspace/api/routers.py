from rest_framework.routers import DefaultRouter
from apps.workspace.api.views.team_views import *
router = DefaultRouter()

router.register(r'team',TeamViewSet, basename = 'Team-view')
urlpatterns = router.urls