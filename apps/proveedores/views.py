from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.proveedores.forms import ProveedorForm
from apps.proveedores.models import Proveedores

from django.http import HttpResponseRedirect


def view_add_proveedor(request):
	info = "informacion"
	if request.method == "POST":
		form = ProveedorForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			info = "Se guardo satisfactoriamente"
			return HttpResponseRedirect('/addProveedores/')
	else:
		formulario = ProveedorForm()
		ctx={'form':formulario}
		return render_to_response('proveedores/addProveedores.html',ctx,context_instance=RequestContext(request))
		
		
def view_delete_proveedor(request,id_proveedor):
	p = Proveedores.objects.filter(id=id_proveedor)
	p.delete()
	return render_to_response('proveedores/rmProveedores.html',context_instance=RequestContext(request))

def view_edit_proveedor(request,id_proveedor):
	proveedor = Proveedores.objects.get(id=id_proveedor)
	if request.method == "GET":
		formulario = ProveedorForm(initial={
						'nombre':proveedor.nombre,
						'apellidoPaterno':proveedor.apellidoMaterno,
						'apellidoMaterno':proveedor.apellidoPaterno,
						'compania':proveedor.compania,
						'telefono':proveedor.telefono,
						'email':proveedor.email,
						})
		ctx = {'form':formulario}
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
		
#	



def view_list_proveedores_edit(request):
	proveedor = Proveedores.objects.filter(status=True)
	ctx={'lista_proveedores':proveedor}
	return render_to_response('proveedores/listProveedoresEdit.html',ctx,context_instance=RequestContext(request))

def view_list_proveedores_delete(request):
	proveedor = Proveedores.objects.filter(status=True)
	ctx={'lista_proveedores':proveedor}
	return render_to_response('proveedores/listProveedoresDel.html',ctx,context_instance=RequestContext(request))
	
