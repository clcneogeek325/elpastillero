from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.pc.views',
	# Examples:
	# url(r'^$', 'elpastillero.views.home', name='home'),
	url(r'^addPC/$', 'view_addPc', name='vista_agregar_pc'),
	url(r'^editPC/(?P<id_pc>.*)/$', 'view_editPc', name='vista_editar_pc'),
	url(r'^rmPC/(?P<id_pc>.*)/$', 'view_rmPc', name='vista_eliminar_pc'),
	
)
