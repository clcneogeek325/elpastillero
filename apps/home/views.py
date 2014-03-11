from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.home.models import Farmacia
from apps.home.forms import FarmaciaForm

from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def about_view(request):
	return render_to_response('about.html',context_instance=RequestContext(request))

def view_add_farmacia(request):
	info = "informacion"
	if request.method == "POST":
		form = FarmaciaForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			info = "Se guardo satisfactoriamente"
			return HttpResponseRedirect('/listFarmacia')
	else:
		formulario = FarmaciaForm()
		ctx = {'form':formulario}
		return render_to_response('home/addFarmacia.html',ctx,context_instance=RequestContext(request))
	
def view_list_farmacia(request):
	farmacia = Farmacia.objects.filter(status=True)
	ctx = {'farmacia':farmacia}
	return render_to_response('home/listFarmacia.html',ctx,context_instance=RequestContext(request))
	
def view_edit_farmacia(request,id_farmacia):
	farmacia = Farmacia.objects.get(id=id_farmacia)
	if request.method == "GET":
		formulario = FarmaciaForm(initial={
						'nombre':farmacia.nombre,
						'direccion':farmacia.direccion,
						'telefono':farmacia.telefono,
						})
		ctx = {'farmacia':farmacia ,'form':formulario}
		return render_to_response('home/editFarmacia.html',ctx,context_instance=RequestContext(request))
	if request.method == "POST":
		farmacia = Farmacia.objects.get(pk=id_farmacia)
		info = "informacion"
		if request.method == "POST":
			form = FarmaciaForm(request.POST,request.FILES,instance=farmacia)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				info = "Se guardo satisfactoriamente"
				return HttpResponseRedirect('/listFarmacia')



