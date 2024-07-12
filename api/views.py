from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Personal, Direccion, Etiqueta , Ticket , Comentario
from .serializers import PersonalSerializer, DireccionesSerializer, EtiquetasSerializer , TicketSerializer, ComentarioSerializer, TicketComentarioSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EtiquetasSerializer
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
        comentarios_data = TicketComentarioSerializer(comentarios, many = True).data
        ticket_data["comentarios"] = comentarios_data

        return Response(ticket_data)

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = (TokenAuthentication,)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:v1')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
