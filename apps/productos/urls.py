from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.productos.views',
    # Examples:
    url(r'^addProductos/$', 'view_add_productos', name='vista_agregar_nuevo_producto'),
    url(r'^editProductos/$', 'view_edit_productos', name='vista_actualizar_producto'),
    url(r'^rmProductos/$', 'view_rm_productos', name='vista_eliminar_producto'),
    url(r'^addMercancia/$', 'view_add_mercancia', name='vista_gregar_mercancia'),
)
