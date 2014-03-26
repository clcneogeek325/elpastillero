from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect

def view_add_mercancia(request):
	if request.user.is_authenticated():
		status_del_producto = "active"
		ctx = {'status_del_producto':status_del_producto}
		return render_to_response('productos/existsProductos/addMercancia.html',ctx,
									context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
