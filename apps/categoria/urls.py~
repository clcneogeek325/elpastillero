from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.categoria.views',
    # Examples:
    # url(r'^$', 'elpastillero.views.home', name='home'),
    url(r'^listaCategoriasDel/$', 'view_list_categoriaDel', name='vista_lista_categorias_eliminar'),
    url(r'^listaCategoriasEdit/$', 'view_list_categoriaEdit', name='vista_lista_categorias_actualizar'),
    url(r'^addCategoria/$', 'view_add_categoria', name='vista_agregar_categoria'),
    url(r'^editCategoria/(?P<id_categoria>.*)/$', 'view_edit_categoria', name='vista_editar_categoria'),
    url(r'^rmCategoria/(?P<id_categoria>.*)/$', 'view_rm_categoria', name='vista_eliminar_categoria'),
 
)
