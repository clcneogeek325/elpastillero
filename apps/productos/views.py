from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from apps.productos.forms import ProductoForm,GetCodigoProductoForm,LoginForm,ProductoFormCompleto,productoSinCodigoForm
from apps.productos.models import Producto,Mejor_proveedor,productoSinCodigo
from apps.mercancia.forms import MercanciaForm,MercanciaSuperForm
from apps.mercancia.models import Mercancia
from django.contrib.auth import login,logout,authenticate


"""
==================================

	FUNCIONES PRODUCTO

==================================
"""

def view_p_sinCodigo_Add(request):
	if request.method == "POST":
		form = productoSinCodigoForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.status = True
			p.save()
		return HttpResponseRedirect("/nuevo/s/%s/"% p.id)
	else:
		print "Fue un GET"
		msg = "Escribe el nombre del producto y presiona Siguiente"
		form = productoSinCodigoForm()
		status_add_producto = "active"
		ctx = {'form':form,
			   'status_add_producto':status_add_producto,
			   'msg':msg}
		return render_to_response('productos/newProductos/sinCodigo/addProducto.html',ctx,
								context_instance=RequestContext(request))

def view_tipo(request):
	status_add_producto = "active"
	ctx = {'status_add_producto':status_add_producto}
	return render_to_response('productos/newProductos/TipoProducto.html',ctx,context_instance=RequestContext(request))


def view_add_producto_nuevo(request,tipo_producto,id_producto):
	form_producto = ProductoForm(initial={'codigo':id_producto})
	existe_prod = productoSinCodigo.objects.filter(pk=id_producto)
	if existe_prod:
		#si existe en la tabla
		prod_sin = productoSinCodigo.objects.get(pk=id_producto)
		form_producto = ProductoForm(initial={'codigo':id_producto,'nombre_producto':prod_sin.nombre_producto})
	if tipo_producto == "f":
		form_mercancia = MercanciaForm()
		#es de tipo farmacia
	else:
		#es diferente a farmacia
		form_mercancia = MercanciaSuperForm()
	if request.method == "POST":
		form_producto = ProductoForm(request.POST)
		form_mercancia = MercanciaForm(request.POST)
		if form_producto.is_valid() and form_mercancia.is_valid():
			p = form_producto.save(commit=False)
			m = form_mercancia.save(commit=False)
			m.producto_id = p.codigo
			m.personal_id = request.user.id
			m.categoria_id = p.categoria_id
			p.total_piezas = m.piezas_compra
			p.precio_compra = m.precio_compra
			p.precio_venta = m.precio_venta
			p.status = True
			p.save()
			m.save()
			mp = Mejor_proveedor(producto_id=p.codigo,proveedor_id=m.proveedor_id,precio=m.precio_compra)
			mp.save()
			mensaje = "Los datos se gusradaron satistactoriamente"
			mensaje_btn  = "Agregar mas productos"
			titulo = "Dar de alta a productos"
			url = "/getCodigoProductoAdd/"
			ctx = {'mensaje':mensaje,
					'titulo':titulo,
				   'mensaje_btn':mensaje_btn,
				   'url':url}
			return render_to_response('productos/newProductos/mensajeProductos.html',ctx,
			context_instance=RequestContext(request))
	else:
		msg = "El producto aun no esta registrado rellene los siguientes campos"
		ctx = {'form_producto':form_producto,
			   'msg':msg,
			   'form_mercancia':form_mercancia}
		return render_to_response('productos/newProductos/addProductos.html',ctx,
						context_instance=RequestContext(request))


def view_add_products_exists(request,tipo_producto,id_producto):
	p = Producto.objects.get(pk=id_producto)
	if tipo_producto == "f":
		form_mercancia = MercanciaForm()
		#es de tipo farmacia
	else:
		#es diferente a farmacia
		form_mercancia = MercanciaSuperForm()
	if request.method == "POST":
		form = MercanciaForm(request.POST)
		if form.is_valid():
			m = form.save(commit=False)
			p.total_piezas += m.piezas_compra
			p.precio_venta = m.precio_venta
			if Mejor_proveedor.objects.filter(producto_id=p.codigo,proveedor_id=m.proveedor_id):
				m_prov = Mejor_proveedor.objects.get(proveedor_id=m.proveedor_id,producto_id=p.codigo)
				m_prov.precio = m.precio_compra
				m_prov.save()
			else:
				mp = Mejor_proveedor(producto_id=p.codigo,proveedor_id=m.proveedor_id,precio=m.precio_compra)
				mp.save()
			lista_provs = Mejor_proveedor.objects.filter(producto_id=p.codigo)
			if lista_provs > 1:
				for recorrido in range(1,len(lista_provs)):
				  for posicion in range(len(lista_provs) - recorrido):
					if lista_provs[posicion].precio > lista_provs[posicion + 1].precio:
					  temp = lista_provs[posicion]
					  lista_provs[posicion] = lista_provs[posicion + 1]
					  lista_provs[posicion + 1] = temp
				mejor_p = []
				mejor_p.append(lista_provs[0])
				p.precio_compra = mejor_p[0].precio
				p.save()
			else:
				p.precio_compra = m.precio_compra
				p.save()
			mensaje = "Los datos se guardaron corramete"
			mensaje_btn = "Agregar mas prodoctos"
			titulo = "Dar de alta productos"
			url = "/getCodigoProductoAdd/"
			ctx = {'mensaje':mensaje,
					'titulo':titulo,
				   'mensaje_btn':mensaje_btn,
				   'url':url}
			return render_to_response('productos/existsProductos/mensajesProductos.html',ctx,
												context_instance=RequestContext(request))
		print "Fue un post"
	else:
		form_mercancia = MercanciaForm()
		msg = "El producto ya  esta registrado pero puede agregar mas mecancia"
		ctx = {'form_mercancia':form_mercancia,
				'msg':msg,
				'p':p}
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
				print "Si existen prodoctos "
				return HttpResponseRedirect("/existente/f/%s/"% id_producto)
			else:
				print "No registrado en el sistema"
				print id_producto
				return HttpResponseRedirect("/nuevo/f/%s/"% id_producto)
	else:
		form  = GetCodigoProductoForm()
		titulo = "Dar de alta productos"
		status_add_producto = "active"
		ctx = {'form':form,
				'titulo':titulo,
				'status_add_producto':status_add_producto}
		return render_to_response('productos/newProductos/get_codigo_producto.html',ctx,
								context_instance=RequestContext(request))

def view_get_IdProductos_super(request):
	info = "inciando" 
	if request.method == "POST":
		print "solo fue un post"
		form = GetCodigoProductoForm(request.POST)
		form_producto = ProductoForm()
		if form.is_valid():
			id_producto = form.cleaned_data['codigo']
			producto = Producto.objects.filter(codigo=id_producto)
			if producto:
				print "Si existen prodoctos "
				return HttpResponseRedirect("/existente/s/%s/"% id_producto)
			else:
				print "No registrado en el sistema"
				print id_producto
				return HttpResponseRedirect("/nuevo/s/%s/"% id_producto)
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
		formulario = ProductoFormCompleto(instance=prod)
		status_del_producto = "active"
		ctx ={'form':formulario,
			  'status_del_producto':status_del_producto}
		return render_to_response('productos/newProductos/rmProductos.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		prod.status = False
		prod.save()
		status_del_producto = "active"
		msg_btn = "Eliminar otro producto"
		msg = "El producto se ha eliminado correctamnete"
		titulo = "Dar de baja productos del sistema"
		url = "/getCodigoProductoDel"
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
		formulario = ProductoFormCompleto(instance=prod)
		status_edit_producto = "active"
		ctx ={'form':formulario,
			'status_edit_producto':status_edit_producto}
		return render_to_response('productos/newProductos/editProductos.html',ctx,
								context_instance=RequestContext(request))
	if request.method == "POST":
		formulario = ProductoFormCompleto(request.POST,request.FILES,instance=prod)
		edit = formulario.save(commit=False)
		edit.status = True
		edit.save()
		status_edit_producto = "active"
		msg_btn = "Actualizar otro producto"
		msg = "Los datos del producto se han actualizado correctamnete"
		titulo = "Dar de baja productos del sistema"
		url = "/getCodigoProductoEdit"
		ctx= {'titulo':titulo,
			'mensaje_btn':msg_btn,
			'mensaje':msg,
			'url':url,
				'status_edit_producto':status_edit_producto}
		return render_to_response('productos/newProductos/mensajeProductos.html',ctx,
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

