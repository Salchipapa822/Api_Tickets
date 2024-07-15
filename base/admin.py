from django.contrib import admin

from . import models


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "autor", "contenido", "fecha_creacion")
    list_filter = ("ticket", "autor")


admin.site.register(models.Etiqueta)
admin.site.register(models.Direccion)
admin.site.register(models.Personal)
admin.site.register(models.Ticket)
admin.site.register(models.Comentario, ComentarioAdmin)
