from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.ventas.views',
    # Examples:
    url(r'^addVentas/(?P<id_producto>.*)/$', 'view_add_ventas', name='vista_agregar_ventas'),
    url(r'^finVenta/$', 'view_vender', name='vista_terminar_venta'),
    url(r'^canclVenta/$', 'view_cancel_venta', name='vista_cancelar_venta'),
    url(r'^delProdVenta/(?P<id_producto>.*)/$', 'view_delt_producto', name='vista_elim_prod_de_venta'),
    url(r'^lstProductosSinCod/$', 'view_ls_p_sin_cod', name='vista_lista_prod_sin_codigo'),
    url(r'^tiket/$', 'view_tiket', name='vista_tiket'),

)
