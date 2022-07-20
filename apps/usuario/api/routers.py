from rest_framework.routers import DefaultRouter
from apps.usuario.api.views.perfil_views import PerfilViewSet
from apps.usuario.api.views.usuario_views import *
from django.urls import path
router = DefaultRouter()

router.register(r'perfil',PerfilViewSet, basename = 'Perfil-view')
urlLogin = [
    path('login/',Login.as_view(),name = 'login'),
    path('logout/',Logout.as_view(),name = 'logout'),
    path('refresh-token/',UserToken.as_view(),name = 'refresh_token'),
]
urlpatterns = router.urls + urlLogin