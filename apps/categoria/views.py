from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria

"""
=======================================================


FUNCIONES CATEGORIA

=========================================================
"""


def view_list_categoriaDel(request):
	lista_de_categorias = obtenerCategorias()
	status_del_producto = "active"
	titulo = "Burcar productos por categoria"
	btn_icon = "icon-remove"
	ctx = {'lista_categorias':lista_de_categorias,
	'status_del_producto':status_del_producto,
	'icono':btn_icon,
	'titulo':titulo}
	return render_to_response('productos/newProductos/listaCategorias.html',ctx,
								context_instance=RequestContext(request))

def view_list_categoriaEdit(request):
	lista_de_categorias = obtenerCategorias()
	status_edit_producto = "active"
	titulo = "Burcar productos por categoria"
	btn_icon = "icon-pencil"
	ctx = {'lista_categorias':lista_de_categorias,
	'status_edit_producto':status_edit_producto,
	'icono':btn_icon,
	'titulo':titulo}
	return render_to_response('productos/newProductos/listaCategorias.html',ctx,
								context_instance=RequestContext(request))



def view_add_categoria(request):
	if request.method == "POST":
		form = CategoriaForm(request.POST,request.FILES)
		if form.is_valid():
			editando = form.save(commit=False)
			editando.status = True
			editando.save()
			status_add_categoria = "active"
			mensaje = "La categoria se ha agregado correctamente"
			titulo = "Agregar una nueva categoria"
			ctx = {'mensaje':mensaje,
			'status_add_categoria':status_add_categoria,
			'titulo':titulo}
			return render_to_response('productos/newProductos/categorias/mensajeCategoria.html',ctx,
									context_instance=RequestContext(request))
	else:
		cats = Categoria.objects.filter(status=True)
		form = CategoriaForm()
		status_add_categoria = "active"
		titulo = "Agregar una nueva categoria"
		ctx = {'form':form,
		'lista_categorias':cats,
		'status_add_categoria':status_add_categoria}
		return render_to_response('productos/newProductos/categorias/addCategorias.html',ctx,
								context_instance=RequestContext(request))


def view_edit_categoria(request,id_categoria):
	cat = Categoria.objects.get(pk=id_categoria)
	if request.method == "POST":
		form  = CategoriaForm(request.POST,request.FILES,instance=cat)
		if form.is_valid():
			editando = form.save(commit=False)
			editando.status = True
			editando.save()
			titulo = "Actualizar datos de una categoria de productos"
			msj = "Los registros se han actualizado corectamente"
			status_add_categoria = "active"
			ctx = {'mensaje':msj,
			'status_add_categoria':status_add_categoria,
			'titulo':titulo}
			return render_to_response('productos/newProductos/categorias/mensajeCategoria.html',ctx,
									context_instance=RequestContext(request))
	else:
		form  = CategoriaForm(instance=cat)
		status_add_categoria = "active"
		ctx = {'form':form,
		'status_add_categoria':status_add_categoria}
		return render_to_response('productos/newProductos/categorias/editCategorias.html',ctx,
									context_instance=RequestContext(request))
		

def view_rm_categoria(request,id_categoria):
	cat = Categoria.objects.get(pk=id_categoria)
	if request.method == "POST":
		cat.delete()
		titulo = "Eliminar una categoria de productos"
		info  = "La categoria se ha eliminado correctamente"
		status_add_categoria = "active"
		ctx = {'mensaje':info,
				'status_add_categoria':status_add_categoria,
				'titulo':titulo}
		return render_to_response('productos/newProductos/categorias/mensajeCategoria.html',ctx,
								context_instance=RequestContext(request))
	else:
		form = CategoriaForm(instance=cat)
		status_add_categoria = "active"
		ctx = {'form':form,
			   'status_add_categoria':status_add_categoria}
		return render_to_response('productos/newProductos/categorias/rmCategorias.html',ctx,context_instance=RequestContext(request))


def obtenerCategorias():
	listaCat = Categoria.objects.filter(status=True)
	return listaCat
