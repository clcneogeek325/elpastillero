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
    url(r'^productoSinCodigoGet/$', 'view_p_sinCodigo_get', name='vista_obtener_Codigo_producto_sin_codigo'),
    url(r'^addProductoSinCodigo/(?P<id_producto>.*)/$', 'view_add_produc_sin_cod', name='vista_agregar_nuevo_producto_sin_codigo'),
    
    url(r'^listaabc/$','view_lista_abc',name='vista_lista_abc'),
    url(r'^busqueda/(?P<letra>.*)/$','view_busqueda',name='vista_busqueda'),
    url(r'^datos_p/(?P<id>.*)/$','view_datos',name='vista_datos'),
    url(r'^busqueda_x_nombre/(?P<nombre>.*)/$','view_busqueda_x_nombre',name='vista_busqueda_x_nombre'),
    url(r'^get_nombre/$','view_get_nombre',name='vista_get_nombre'),
    url(r'^busqueda_x_categoria/(?P<id>.*)/$','view_busqueda_x_categoria',name='vista_busqueda_x_categoria'),

)
