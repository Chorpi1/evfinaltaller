from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from gestion.models import Producto

class Command(BaseCommand):
    help = "Crear grupos de Administradores y Empleados con permisos predefinidos"

    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name="Administradores")
        if created:
            permisos = Permission.objects.all()
            admin_group.permissions.set(permisos)
            self.stdout.write(self.style.SUCCESS('Grupo "Administradores" creado con todos los permisos.'))

        empleado_group, created = Group.objects.get_or_create(name="Empleados")
        if created:
            content_type = ContentType.objects.get_for_model(Producto)
            permisos_ver = Permission.objects.filter(content_type=content_type, codename__startswith="view")
            empleado_group.permissions.set(permisos_ver)
            self.stdout.write(self.style.SUCCESS('Grupo "Empleados" creado con permisos de solo visualización.'))
