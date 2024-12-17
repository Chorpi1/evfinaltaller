from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from gestion.models import Producto

# Registro del modelo Producto en el panel de administrador
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_unitario', 'fecha_vencimiento', 'stock', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nombre']

# Configuración inicial de grupos
def configurar_grupos():
    # Crear o actualizar el grupo "Administradores"
    admin_group, created = Group.objects.get_or_create(name="Administradores")
    if created:
        permisos = Permission.objects.all()
        admin_group.permissions.set(permisos)

    # Crear o actualizar el grupo "Empleados"
    empleado_group, created = Group.objects.get_or_create(name="Empleados")
    if created:
        content_type = ContentType.objects.get_for_model(Producto)
        permisos_ver = Permission.objects.filter(content_type=content_type, codename__startswith="view")
        empleado_group.permissions.set(permisos_ver)

    Group.objects.get_or_create(name="Administradores")
    Group.objects.get_or_create(name="Empleados")



# Ejecutar configuración de grupos
configurar_grupos()
