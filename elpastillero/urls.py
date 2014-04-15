from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elpastillero.views.home', name='home'),
	url(r'^', include('apps.home.urls')),
	url(r'^', include('apps.Personal.urls')),
	url(r'^', include('apps.proveedores.urls')),
	url(r'^', include('apps.productos.urls')),
	url(r'^', include('apps.mercancia.urls')),
	url(r'^', include('apps.categoria.urls')),
	url(r'^', include('apps.compania.urls')),
	url(r'^', include('apps.ventas.urls')),
	url(r'^', include('apps.reportes.urls')),
	url(r'^', include('apps.pc.urls')),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)



