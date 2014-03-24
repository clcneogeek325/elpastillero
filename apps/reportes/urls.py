from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.reportes.views',
    # Examples:
    url(r'^pdf/$', 'view_ejemplo_pdf', name='vista_pdf'),
    url(r'^mejorProveedor/$', 'view_mejorProv', name='vista_mejor_proveedor'),
    
)
