from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.productos.forms import ProductoForm
from apps.productos.models import Producto


def view_add_productos(request):
	info = "informacion"
	if request.method == "POST":
		form = ProductoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			info = "Se guardo satisfactoriamente"
			ctx= {'mensaje':info}
			return render_to_response('productos/newProductos/mensajeAdd.html',ctx,context_instance=RequestContext(request))
	else:
		formulario = ProductoForm()
		ctx = {'form':formulario}
		return render_to_response('productos/newProductos/addProductos.html',ctx,context_instance=RequestContext(request))
		



def view_edit_productos(request):
	return render_to_response('productos/newProductos/editProductos.html',context_instance=RequestContext(request))

def view_rm_productos(request):
	return render_to_response('productos/newProductos/rmProductos.html',context_instance=RequestContext(request))

def view_add_mercancia(request):
	return render_to_response('productos/existsProductos/addMercancia.html',context_instance=RequestContext(request))
	
