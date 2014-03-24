from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.productos.views',
    # Examples:
    url(r'^getCodigoProductoAddFarmacia/$', 'view_get_IdProductos', name='vista_obtener_codigo_agregar'),
    url(r'^getCodigoProductoAddSuper/$', 'view_get_IdProductos_super', name='vista_obtener_codigo_agregar_super'),
    url(r'^listEditProductos/$', 'view_list_edit_productos', name='vista_actualizar_producto'),
    url(r'^listRmProductos/$', 'view_list_rm_productos', name='vista_eliminar_producto'),
    url(r'^getCodigoProductoDel/$', 'view_getCodigoForm_eliminar', name='vista_obtener_codigo_eliminar'),
    url(r'^rmProducto/(?P<codigo_barras>.*)/$', 'view_rm_producto', name='vista_id_produto'),
    url(r'^editProducto/(?P<codigo_barras>.*)/$', 'view_edit_productos', name='vista_editar_productos'),
    url(r'^getCodigoProductoEdit/$', 'view_getCodigoForm_actualizar', name='vista_obtener_codigo_actualizar'),
    url(r'^listaProductos/$', 'view_list_products', name='vista_lista_productos'),
    url(r'^nuevo/(?P<tipo_producto>.*)/(?P<id_producto>.*)/$', 'view_add_producto_nuevo', name='vista_agregar_nuevo_producto'),
    url(r'^existente/(?P<tipo_producto>.*)/(?P<id_producto>.*)/$', 'view_add_products_exists', name='vista_agregar_producto_existenete'),
    url(r'^login/$', 'view_login', name='vista_logearse'),
    url(r'^logout/$', 'view_logout', name='vista_deslogearse'),
    url(r'^tipo/$', 'view_tipo', name='vista_tipo_producto'),
    url(r'^productoSinCodigoAdd/$', 'view_p_sinCodigo_Add', name='vista_agregar_p_sinCodigo'),
    
)
