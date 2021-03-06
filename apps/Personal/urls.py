from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.Personal.views',
    # Examples:
 	url(r'^addPersonal/$', 'view_add_personal', name='vista_agregar_personal'),
	url(r'^editPersonal/(?P<id_personal>.*)/$', 'view_refresh_personal', name='vista_actualizar_personal'),
	url(r'^rmPersonal/(?P<id_personal>.*)/$', 'view_delete_personal', name='vista_eliminar_personal'),
	url(r'^listPersonalDel/$', 'view_list_personal_delete', name='vista_lista_personal_eliminar'),
	url(r'^listPersonalEdit/$', 'view_list_personal_edit', name='vista_lista_personal_actualizar'),
	url(r'^editPasswd/(?P<id_user>.*)/$', 'view_change_paswd', name='vista_cambiar_contrasenia'),
	url(r'^addRoot/(?P<id_user>.*)/$', 'view_add_root', name='vista_agregar_poersmisos'),
)
