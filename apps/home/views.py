from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.home.models import Farmacia
from apps.home.forms import FarmaciaForm
from django.http import HttpResponseRedirect

def obtenerFarmacias():
	return Farmacia.objects.filter(status=True)
	

def index_view(request):
	if request.user.is_authenticated():
		return render_to_response('index.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def comprobar_existencia():
	if Farmacia.objects.exists():
		return False #aun no existen registros que se muestte la opcio de agregar ebn la palntilla
	else:
		return True  #aun no exiten refistros

def view_add_farmacia(request):
	if request.user.is_authenticated() and request.user.is_staff:
		info = "informacion"
		if request.method == "POST":
			form = FarmaciaForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				info = "Se guardo satisfactoriamente"
				status_lista = "active"
				lista_farmacia = obtenerFarmacias()
				existencia = comprobar_existencia()
				ctx = {'existencia':existencia,"farmacia":lista_farmacia,"status_lista":status_lista}
				return render_to_response('home/listFarmacia.html',ctx,context_instance=RequestContext(request))
			else:
				formulario = FarmaciaForm()
				status_add = "active"
				existencia = comprobar_existencia()
				ctx = {'existencia':existencia,'form':formulario,'status_add':status_add}
				return render_to_response('home/addFarmacia.html',ctx,context_instance=RequestContext(request))
		else:
			formulario = FarmaciaForm()
			status_add = "active"
			existencia = comprobar_existencia()
			ctx = {'existencia':existencia,'form':formulario,'status_add':status_add}
			return render_to_response('home/addFarmacia.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
	
def view_list_farmacia(request):
	if request.user.is_authenticated() and request.user.is_staff:
		farmacia = Farmacia.objects.filter(status=True)
		status_lista = "active"
		existencia = comprobar_existencia()
		ctx = {'existencia':existencia,'farmacia':farmacia,'status_lista':status_lista}
		return render_to_response('home/listFarmacia.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		

def view_edit_farmacia(request,id_farmacia):
	if request.user.is_authenticated() and request.user.is_staff:
		farmacia = Farmacia.objects.get(id=id_farmacia)
		if request.method == "GET":
			formulario = FarmaciaForm(initial={
							'nombre':farmacia.nombre,
							'direccion':farmacia.direccion,
							'telefono':farmacia.telefono,
							})
			status_lista = "active"
			existencia = comprobar_existencia()
			ctx = {'existencia':existencia,'farmacia':farmacia ,'form':formulario,"status_lista":status_lista}
			return render_to_response('home/editFarmacia.html',ctx,context_instance=RequestContext(request))
		if request.method == "POST":
			farmacia = Farmacia.objects.get(pk=id_farmacia)
			info = "informacion"
			form = FarmaciaForm(request.POST,request.FILES,instance=farmacia)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				info = "Se guardo satisfactoriamente"
				status_lista = "active"
				existencia = comprobar_existencia()
				farmacias = Farmacia.objects.filter(status=True)
				ctx = {'existencia':existencia,
				"farmacia":farmacias,
				"status_lista":status_lista}
				return render_to_response('home/listFarmacia.html',ctx,
				context_instance=RequestContext(request))
			else:
				formulario = FarmaciaForm(initial={
								'nombre':farmacia.nombre,
								'direccion':farmacia.direccion,
								'telefono':farmacia.telefono,
								})
				status_lista = "active"
				existencia = comprobar_existencia()
				ctx = {'existencia':existencia,
				'farmacia':farmacia ,'form':formulario,
				"status_lista":status_lista}
				return render_to_response('home/editFarmacia.html',ctx,
				context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')



