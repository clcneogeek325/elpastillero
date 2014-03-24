from django.shortcuts import render_to_response
from django.template import RequestContext 


def view_add_mercancia(request):
	status_del_producto = "active"
	ctx = {'status_del_producto':status_del_producto}
	return render_to_response('productos/existsProductos/addMercancia.html',ctx,
								context_instance=RequestContext(request))
