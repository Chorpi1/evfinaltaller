from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('enviar_contacto/', views.enviar_contacto, name='enviar_contacto'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('gestion/', views.gestion, name='gestion'),
    path('gestion-filtrada/', views.gestion_filtrada, name='gestion_filtrada'),  # Vista con filtro
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar-producto/', views.editar_producto, name='editar_producto'),
    path('procesar-venta/', views.procesar_venta, name='procesar_venta'),
    path('verificar-stock/<int:producto_id>/', views.verificar_stock, name='verificar_stock'),
    path('reporte-pdf/', views.generar_reporte_pdf, name='reporte_pdf'),
    path('reporte-excel/', views.generar_reporte_excel, name='reporte_excel'),
]
