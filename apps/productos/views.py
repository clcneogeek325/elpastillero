from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from apps.productos.forms import ProductoForm,GetCodigoProductoForm,LoginForm
from apps.productos.models import Producto
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from apps.mercancia.forms import MercanciaForm
from django.contrib.auth import login,logout,authenticate


"""
==================================

	FUNCIONES PRODUCTO

==================================
"""


def view_login(request):
	msg = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	else:
		if request.method == "POST":
			form  = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['passwd']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					msg = "Usuario y/o paswords incorrectos"
	form = LoginForm()
	ctx = {'form':form,'msg':msg}
	return render_to_response('login/login.html',ctx,context_instance=RequestContext(request))

def view_logout(request):
	logout(request)
	return HttpResponseRedirect('/login')


def view_add_producto_nuevo(request,id_producto):
	form_producto = ProductoForm(initial={'codigo':id_producto})
	form_mercancia = MercanciaForm()
	if request.method == "POST":
		form_producto = ProductoForm(request.POST)
		form_mercancia = MercanciaForm(request.POST)
		if form_producto.is_valid() and form_mercancia.is_valid():
			print "Los 2 formularios son validos'"
	else:
		msg = "El producto aun no esta registrado rellene los siguientes campos"
		ctx = {'form_producto':form_producto,
			   'msg':msg,
			   'form_mercancia':form_mercancia}
		return render_to_response('productos/newProductos/addProductos.html',ctx,
						context_instance=RequestContext(request))


def view_add_producto_existente(request,id_producto):
	producto = Producto.objects.get(pk=id_producto)
	if request.method == "POST":
		print "Fue un post"
	else:
		form_mercancia = MercanciaForm(instance=producto)
		ctx = {'form_mercancia':form_mercancia}
		print "Fue un get"
		return render_to_response('productos/existsProductos/addMercancia.html',ctx,
									context_instance=RequestContext(request))



def view_get_IdProductos(request):
	info = "inciando" 
	
	if request.method == "POST":
		print "solo fue un post"
		form = GetCodigoProductoForm(request.POST)
		form_producto = ProductoForm()
		if form.is_valid():
			id_producto = form.cleaned_data['codigo']
			producto = Producto.objects.filter(codigo=id_producto)
			if producto:
				print "Si existen prodoctos"
			else:
				print "No registrado en el sistema"
				print id_producto
				return HttpResponseRedirect("/nuevo/%s/"% id_producto)
	else:
		form  = GetCodigoProductoForm()
		titulo = "Dar de alta productos"
		status_add_producto = "active"
		ctx = {'form':form,
				'titulo':titulo,
				'status_add_producto':status_add_producto}
		return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
								context_instance=RequestContext(request))

def view_getCodigoForm_eliminar(request):
	if request.method == "GET":
		form  = GetCodigoProductoForm()
		titulo = "Dar de baja a un producto"
		status_del_producto = "active"
		ctx = {'form':form,
				'titulo':titulo,
				'status_del_producto':status_del_producto}
		return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		form = GetCodigoProductoForm(request.POST)
		if form.is_valid():
			codigo = form.cleaned_data['codigo']
			return HttpResponseRedirect("/rmProducto/%s"%codigo)
		else:
			form  = GetCodigoProductoForm()
			status_del_producto = "active"
			titulo = "Dar de baja a un producto"
			ctx = {'form':form,
					'titulo':titulo,
					'status_del_producto':status_del_producto}
			return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
										context_instance=RequestContext(request))
				
				

def view_getCodigoForm_actualizar(request):
	if request.method == "GET":
		form  = GetCodigoProductoForm()
		status_edit_producto = "active"
		titulo = "Actualizar datos de un producto"
		ctx = {'form':form,
				'titulo':titulo,
				'status_edit_producto':status_edit_producto}
		return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		form = GetCodigoProductoForm(request.POST)
		if form.is_valid():
			codigo = form.cleaned_data['codigo']
			return HttpResponseRedirect("/editProducto/%s"%codigo)
		else:
			form  = GetCodigoProductoForm()
			status_edit_producto = "active"
			titulo = "Actualizar datos de un producto"
			ctx = {'form':form,
					'titulo':titulo,
					'status_edit_producto':status_edit_producto}
			return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
								context_instance=RequestContext(request))
				
				
				
def view_rm_producto(request,codigo_barras):
	prod = Producto.objects.get(pk=codigo_barras)
	if request.method == "GET":
		formulario = ProductoForm(instance=prod)
		status_del_producto = "active"
		ctx ={'form':formulario,
			  'status_del_producto':status_del_producto}
		return render_to_response('productos/newProductos/rmProductos.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		prod.delete()
		status_del_producto = "active"
		msg_btn = "Eliminar otro producto"
		msg = "El producto se ha eliminado correctamnete"
		titulo = "Dar de baja productos del sistema"
		url = "/listRmProductos"
		ctx= {'titulo':titulo,
			'mensaje_btn':msg_btn,
			'mensaje':msg,
			'url':url,
			'status_del_producto':status_del_producto}
		return render_to_response('productos/newProductos/mensajeProductos.html',ctx,
								context_instance=RequestContext(request))
			
def view_list_edit_productos(request):
	status_edit_producto = "active"
	ctx = {'status_edit_producto':status_edit_producto}
	return render_to_response('productos/newProductos/listEditProductos.html',ctx,
								context_instance=RequestContext(request))

def view_list_rm_productos(request):
	status_del_producto = "active"
	ctx = {'status_del_producto':status_del_producto}
	return render_to_response('productos/newProductos/listDelProductos.html',ctx,
								context_instance=RequestContext(request))




def view_edit_productos(request,codigo_barras):
	prod = Producto.objects.get(pk=codigo_barras)
	if request.method == "GET":
		print codigo_barras,"este es un get"
		formulario = ProductoForm(instance=prod)
		status_edit_producto = "active"
		ctx ={'form':formulario,
			'status_edit_producto':status_edit_producto}
		return render_to_response('productos/newProductos/editProductos.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		formulario = ProductoForm(request.POST,request.FILES,instance=prod)
		edit = formulario.save(commit=False)
		edit.status = True
		edit.save()
		formulario.save_m2m()
		status_edit_producto = "active"
		msg_btn = "Actualizar otro producto"
		msg = "Los datos del producto se han actualizado correctamnete"
		titulo = "Dar de baja productos del sistema"
		url = "/listEditProductos"
		ctx= {'titulo':titulo,
			'mensaje_btn':msg_btn,
			'mensaje':msg,
			'url':url,
				'status_edit_producto':status_edit_producto}
		return render_to_response('productos/newProductos/mensajeEdit.html',ctx,
								context_instance=RequestContext(request))
		

def view_list_products(request):
	lista_productos = Producto.objects.filter(status=True)
	titulo = "Lista de productos"
	btn_icon = "icon-pencil"
	ctx = {'lista_productos':lista_productos,
			'titulo':titulo,
			'icono':btn_icon}
	return render_to_response('productos/newProductos/listaProductos.html',ctx,
							context_instance=RequestContext(request))
