from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.ws.views',
    # Examples:
    url(r'^ws/prod/buscar/(?P<dato>.*)/$', 'ws_buscar_producto', name='servicio_buscar_producto'),
    url(r'^ws/mercancia/$', 'ws_ultimos_registros', name='servicio_mercancia'),
    url(r'^ws/prov/(?P<id>.*)/$', 
            'ws_buscar_proveedor_de_compania', 
            name='servicio_buscar_producto'),


    url(r'^ws/producto/(?P<id>.*)/$', 
            'ws_producto', 
            name='servicio_producto_id'),
)
