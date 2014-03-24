from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.proveedores.views',
    # Examples:
    url(r'^addProveedores/$', 'view_add_proveedor', name='vista_agregar_proveedor'),
    url(r'^editProveedor/(?P<id_proveedor>.*)/$', 'view_edit_proveedor', name='vista_actualizar_proveedor'),
    url(r'^rmProveedor/(?P<id_proveedor>.*)/$', 'view_delete_proveedor', name='vista_eliminar_proveedor'),
    url(r'^listProveedoresEdit/$', 'view_list_proveedores_edit', name='vista_lista_proveedores_actualizar'),
    url(r'^listProveedoresDel/$', 'view_list_proveedores_delete', name='vista_lista_proveedores_eliminar'),
    
)
