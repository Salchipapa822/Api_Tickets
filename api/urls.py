from django.urls import include, path
from django.contrib.auth.models import User
from .views import PersonalViewSet, DireccionesViewSet, EtiquetasViewSet , TicketsViewSet , ComentariosViewSet, UsersViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"personal", PersonalViewSet)
router.register(r"direcciones", DireccionesViewSet)
router.register(r"etiquetas", EtiquetasViewSet)
router.register(r"tickets", TicketsViewSet)
router.register(r"comentarios", ComentariosViewSet)
router.register(r"Tecnicos", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
