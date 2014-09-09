from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria
from django.http import HttpResponseRedirect
"""
=======================================================


FUNCIONES CATEGORIA

=========================================================
"""


def view_list_categoriaDel(request):
	if request.user.is_authenticated():
		lista_de_categorias = obtenerCategorias()
		status_del_producto = "active"
		titulo = "Burcar productos por categoria"
		btn_icon = "icon-remove"
		ctx = {'lista_categorias':lista_de_categorias,
		'status_del_producto':status_del_producto,
		'icono':btn_icon,
		'titulo':titulo,'status_categoria':'active'}
		return render_to_response('categorias/listaCategorias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_list_categoriaEdit(request):
	if request.user.is_authenticated():
		lista_de_categorias = obtenerCategorias()
		status_edit_producto = "active"
		titulo = "Burcar productos por categoria"
		btn_icon = "icon-pencil"
		ctx = {'lista_categorias':lista_de_categorias,
		'status_edit_producto':status_edit_producto,
		'icono':btn_icon,
		'titulo':titulo,'status_categoria':'active'}
		return render_to_response('categorias/listaCategorias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')



def view_add_categoria(request):
	if request.user.is_authenticated():
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
				'titulo':titulo,'status_categoria':'active'}
				return render_to_response('categorias/mensajeCategoria.html',ctx,
										context_instance=RequestContext(request))
			else:			
				cats = Categoria.objects.filter(status=True)
				form = CategoriaForm()
				mensaje = "Escribe un nombre  de categoria"
				status_add_categoria = "active"
				titulo = "Agregar una nueva categoria"
				ctx = {'form':form,
				'lista_categorias':cats,
				'status_add_categoria':status_add_categoria,'status_categoria':'active'}
				return render_to_response('categorias/addCategorias.html',ctx,
										context_instance=RequestContext(request))


		else:
			cats = Categoria.objects.filter(status=True)
			form = CategoriaForm()
			status_add_categoria = "active"
			titulo = "Agregar una nueva categoria"
			ctx = {'form':form,
			'lista_categorias':cats,
			'status_add_categoria':status_add_categoria,'status_categoria':'active'}
			return render_to_response('categorias/addCategorias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')


def view_edit_categoria(request,id_categoria):
	if request.user.is_authenticated():
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
				'titulo':titulo,'status_categoria':'active'}
				return render_to_response('categorias/mensajeCategoria.html',ctx,
										context_instance=RequestContext(request))
		else:
			form  = CategoriaForm(instance=cat)
			status_add_categoria = "active"
			ctx = {'form':form,
			'status_add_categoria':status_add_categoria,
			'status_categoria':'active'}
			return render_to_response('categorias/editCategorias.html',ctx,
										context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_rm_categoria(request,id_categoria):
	if request.user.is_authenticated():
		cat = Categoria.objects.get(pk=id_categoria)
		if request.method == "POST":
			cat.status = False
			titulo = "Eliminar una categoria de productos"
			info  = "La categoria se ha eliminado correctamente"
			status_add_categoria = "active"
			ctx = {'mensaje':info,
					'status_add_categoria':status_add_categoria,
					'titulo':titulo,'status_categoria':'active'}
			return render_to_response('categorias/mensajeCategoria.html',ctx,
									context_instance=RequestContext(request))
		else:
			form = CategoriaForm(instance=cat)
			status_add_categoria = "active"
			ctx = {'form':form,
				   'status_add_categoria':status_add_categoria,'status_categoria':'active'}
			return render_to_response('categorias/rmCategorias.html',
									ctx,context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/login')


def obtenerCategorias():
	listaCat = Categoria.objects.filter(status=True)
	return listaCat
