from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Personal,Direccion, Etiqueta , Ticket , Comentario

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id',
                  'nombre')

class EtiquetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ('id',
                  'nombre')

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
            'cedula',
            'nombre',
            'apellido',
        )
        

        
class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Comentario
        fields = "__all__"
        read_only_fields = ('fecha_creacion',)


class TicketComentarioSerializer(ComentarioSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comentarios')  

    class Meta:
        model = Comentario
        fields = ('id', 'contenido', 'autor', 'fecha_creacion')


class TicketSerializer(serializers.ModelSerializer):
    presentado_por = serializers.StringRelatedField(many=False)
    resuelto_por = serializers.StringRelatedField(many=False)
    presentado_en = serializers.StringRelatedField(many=False)
    etiqueta = serializers.StringRelatedField(many=False)
    comentarios_count = serializers.SerializerMethodField()


    def get_comentarios_count(self, ticket):
        return ticket.comentarios.count()
    
    class Meta:
        model = Ticket
        fields = (
            'id' ,
            'titulo' ,
            'fecha_creacion' ,
            'fecha_cierre' ,
            'presentado_por' ,
            'resuelto_por' ,
            'presentado_en',
            'etiqueta' ,
            'comentarios_count',
        )
        read_only_fields = ('fecha_creacion',)