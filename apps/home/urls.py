from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.home.views',
    # Examples:
    url(r'^$', 'index_view', name='vista_inicio'),
    url(r'^addFarmacia/$', 'view_add_farmacia', name='vista_agregar_farmacia'),
    url(r'^listFarmacia/$', 'view_list_farmacia', name='vista_lista_farmacia'),
    url(r'^editFarmacia/(?P<id_farmacia>.*)/$', 'view_edit_farmacia', name='vista_actualizar_farmacia'),
    
    #url(r'^about/$', 'about_view', name='vista_acercade'),
    
)
