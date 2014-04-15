from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.proveedores.forms import ProveedorForm
from apps.proveedores.models import Proveedores
from django.http import HttpResponseRedirect


titulo_add = "Agregar un nuevo proveedor"
titulo_edit = "Actulizar datos de un proveedor"
titulo_del = "Eliminar un proveedor"


msg_add = "El registro se ha agregado correctamente"
msg_edit = "El registro se ha actualizado"
msg_del = "El registro se ha eliminado"

def view_add_proveedor(request):
	if request.user.is_authenticated() and request.user.is_staff:
		info = "informacion"
		if request.method == "POST":
			form = ProveedorForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				formulario = ProveedorForm()
				url = "/addProveedores"
				status_agregar = "active"
				msg_btn = "Agregar otro proveedor"
				ctx={'status_agregar':status_agregar,
					 'titulo':titulo_add,
					 'mensaje':msg_add,
					 'url':url ,
					 'msg_btn':msg_btn}
				return render_to_response('proveedores/mensajes.html',ctx,
						context_instance=RequestContext(request))
			else:
				formulario = ProveedorForm()
				msg = "Ups lo sentimos el usuario no se pudo agregregar \
					probablemente por que algun campo bno esta lleno o la informacion es incorrecta"
				status_agregar = "active"
				ctx={'form':formulario,
					'msg':msg,
					 'status_agregar':status_agregar}
				return render_to_response('proveedores/addProveedores.html',ctx,
							context_instance=RequestContext(request))
		else:
			formulario = ProveedorForm()
			status_agregar = "active"
			msg = "Llene los siguinetes campoos para agregar un nuevo proveedor"
			ctx={'form':formulario,
				'msg':msg,
				 'status_agregar':status_agregar}
			return render_to_response('proveedores/addProveedores.html',ctx,
						context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		
def view_delete_proveedor(request,id_proveedor):
	if request.user.is_authenticated() and request.user.is_staff:
		p = Proveedores.objects.filter(id=id_proveedor)
		p.status = False
		status_eliminar = "active"
		msg_btn = "Regresar a la lista"
		url = "/listProveedoresDel"
		ctx = {'mensaje':msg_del,
			   'titulo':titulo_del,
			   'url':url,
			   'msg_btn':msg_btn,
			   'status_eliminar':status_eliminar}
		return render_to_response('proveedores/mensajes.html',ctx,
						context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		
		
def view_edit_proveedor(request,id_proveedor):
	if request.user.is_authenticated() and request.user.is_staff:
		proveedor = Proveedores.objects.get(id=id_proveedor)
		if request.method == "GET":
			formulario = ProveedorForm(instance=proveedor)
			status_actualizar = "active"
			ctx = {'form':formulario,'status_actualizar':status_actualizar}
			return render_to_response('proveedores/editProveedores.html',ctx,context_instance=RequestContext(request))
		if request.method == "POST":
			info = "informacion"
			form = ProveedorForm(request.POST,request.FILES,instance=proveedor)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				info = "Se guardo satisfactoriamente"
				return HttpResponseRedirect('/listProveedoresEdit')
	else:
		return HttpResponseRedirect('/login')
	

def view_list_proveedores_edit(request):
	if request.user.is_authenticated() and request.user.is_staff:
		proveedor = Proveedores.objects.filter(status=True)
		status_actualizar = "active"
		ctx={'lista_proveedores':proveedor,
			 'status_actualizar':status_actualizar}
		return render_to_response('proveedores/listProveedoresEdit.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		
		
		
def view_list_proveedores_delete(request):
	if request.user.is_authenticated() and request.user.is_staff:
		provs = Proveedores.objects.filter(status=True) 
		status_eliminar = "active"
		ctx={'lista_proveedores':provs,
			 'status_eliminar':status_eliminar}
		return render_to_response('proveedores/listProveedoresDel.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
