from django.contrib.auth import logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Comentario, Direccion, Etiqueta, Personal, Ticket

from .serializers import (ComentarioSerializer, DireccionesSerializer,
                          EtiquetasSerializer, PersonalSerializer,
                          TicketComentarioSerializer, TicketSerializer,
                          UsersSerializer)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)


class DireccionesViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)


class EtiquetasViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)

    @action(detail=True,)
    def comentarios(self, request, pk=None):
        ticket = self.get_object()
        ticket_data = self.get_serializer(ticket).data
        comentarios = Comentario.objects.filter(ticket=ticket)
        comentarios_data = TicketComentarioSerializer(
            comentarios, many=True).data
        ticket_data["comentarios"] = comentarios_data

        return Response(ticket_data)


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)






