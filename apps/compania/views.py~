from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.compania.models import Compania
from apps.compania.forms import CompaniaForm
from django.http import HttpResponseRedirect

"""
=======================================================


FUNCIONES COMPANIA

=========================================================
"""

def view_listCompaniaDel(request):
	if request.user.is_authenticated():
		lista_de_companias = obtenerCompanias()
		status_del_producto = "active"
		titulo = "Burcar productos por Companias"
		btn_icon = "icon-remove"
		ctx = {'lista_companias':lista_de_companias,
				'status_del_producto':status_del_producto,
				'icono':btn_icon,
				'titulo':titulo}
		return render_to_response('productos/newProductos/listaCompanias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_listCompaniaEdit(request):
	if request.user.is_authenticated():
		lista_de_companias = obtenerCompanias()
		status_edit_producto = "active"
		titulo = "Buscar Peoductos por Companias"
		btn_icon = "icon-pencil"
		ctx = {'lista_companias':lista_de_companias,
				'status_edit_producto':status_edit_producto,
				'icono':btn_icon,
				'titulo':titulo}
		return render_to_response('productos/newProductos/listaCompanias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def obtenerCompanias():
	listCompan = Compania.objects.filter(status=True)
	return listCompan

def view_rm_compania(request,id_compania):
	if request.user.is_authenticated():
		status_add_compania = "active"
		compania = Compania.objects.get(pk=id_compania)
		if request.method == "POST":
			compania.delete()
			titulo = "Eliminar una compania"
			info = "El registro se elimino correctamente"
			ctx = {'mensaje':info,
					'status_add_compania':status_add_compania,
					'titulo':titulo}
			return render_to_response('productos/newProductos/companias/mensajeCompania.html',ctx,
									context_instance=RequestContext(request))
		else:
			form = CompaniaForm(instance=compania)
			ctx = {'form':form,
					'status_add_compania':status_add_compania}
			return render_to_response('productos/newProductos/companias/rmCompanias.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')



def view_edit_compania(request,id_compania):
	if request.user.is_authenticated():
		compania = Compania.objects.get(pk=id_compania)
		if request.method == "POST":
			form  = CompaniaForm(request.POST,request.FILES,instance=compania)
			if form.is_valid():
				edit = form.save(commit=False)
				edit.status = True
				edit.save()
				titulo = "Corregir el nombre de una compania"
				info = "Los datos se guardaron correctamente"
				status_add_compania = "active"
				ctx = {"mensaje":info,
						'status_add_compania':status_add_compania,
						'titulo':titulo}
				return render_to_response('productos/newProductos/companias/mensajeCompania.html',ctx,
										context_instance=RequestContext(request))
		else:
			form = CompaniaForm(instance=compania)
			status_add_compania = "active"
			ctx = {'form':form,
			'status_add_compania':status_add_compania}
			return render_to_response('productos/newProductos/companias/editCompanias.html',ctx,
										context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')



def view_add_compania(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CompaniaForm(request.POST,request.FILES)
			if form.is_valid():
				edit= form.save(commit=False)
				edit.status = True
				edit.save()
				titulo = "Agregar una nueva compania"
				info = "La compania de agrego correctamente"
				status_add_compania = "active"
				ctx = {'mensaje':info,
				'status_add_compania':status_add_compania,
				'titulo':titulo}
				return render_to_response('productos/newProductos/companias/mensajeCompania.html',
										ctx,context_instance=RequestContext(request))
		else:
			lista_de_companias = obtenerCompanias()
			form = CompaniaForm()
			status_add_compania = "active"
			ctx = {'form':form,
			'lista_companias':lista_de_companias,
			'status_add_compania':status_add_compania}
			return render_to_response('productos/newProductos/companias/addCompanias.html',
										ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
