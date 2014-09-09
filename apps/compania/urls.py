from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.compania.views',
    # Examples:
    # url(r'^$', 'elpastillero.views.home', name='home'),
    url(r'^listCompaniasDel/$', 'view_listCompaniaDel', name='vista_lista_companias_eliminar'),
    url(r'^listCompaniasEdit/$', 'view_listCompaniaEdit', name='vista_lista_companias_actualizar'),
    url(r'^addCompania/$', 'view_add_compania', name='vista_agregar_compania'),
    url(r'^editCompania/(?P<id_compania>.*)/$', 'view_edit_compania', name='vista_editar_compania'),
    url(r'^rmCompania/(?P<id_compania>.*)/$', 'view_rm_compania', name='vista_eliminar_compania'),
 
)
