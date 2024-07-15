from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api_v1.views import Login, Logout

from .views import (ComentariosViewSet, DireccionesViewSet, EtiquetasViewSet,
                    PersonalViewSet, TicketsViewSet, UsersViewSet)

router = routers.DefaultRouter()
router.register(r"personal", PersonalViewSet)
router.register(r"direcciones", DireccionesViewSet)
router.register(r"etiquetas", EtiquetasViewSet)
router.register(r"tickets", TicketsViewSet)
router.register(r"comentarios", ComentariosViewSet)
router.register(r"tecnicos", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view()),
]
