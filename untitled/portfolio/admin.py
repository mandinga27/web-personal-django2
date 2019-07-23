from django.contrib import admin
from.models import Project

# Register your models here.

#con esta clase se puede ver de forma de lectura la fecha de craecion y edicion del proyecto en la pag admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')






#aca se registra en la web del admin el modelo creado anteriormente 'Project'
#sse debe pasar el nombre de la clase 'ProjectAdmin' para que la muestre en la pag admin
admin.site.register(Project, ProjectAdmin)