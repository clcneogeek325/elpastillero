from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.Personal.forms import addPersonalForm
from apps.Personal.models import Personal
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from apps.Personal.forms import UserForm

def view_add_personal(request):
	info = "informacion"
	if request.method == "POST":
		form_personal = addPersonalForm(request.POST)
		form_user = UserForm(request.POST)
		if form_personal.is_valid() and form_user.is_valid():
			addp = form_personal.save(commit=False)
			addp.status = True
			addp.save()
			nombre_usuario = form_user.cleaned_data['user']
			contrasenia =  form_user.cleaned_data['password']
			correo = addp.email
			u = User.objects.create_user(username=nombre_usuario,email=correo,password=contrasenia)
			u.save()
			info = "Se guardo satisfactoriamente"
			status_agregar = "active"
			ctx = {'status_agregar':status_agregar,
			'msg':info}
			return render_to_response('personal/mensaje.html',ctx,context_instance=RequestContext(request))
	else:
		form_personal = addPersonalForm()
		form_user = UserForm()
		status_agregar = "active"
		ctx = {'form_user':form_user,
		'form_personal':form_personal,
		'status_agregar':status_agregar}
		return render_to_response('personal/addPersonal.html',ctx,context_instance=RequestContext(request))

def view_refresh_personal(request,id_personal):
	personal = Personal.objects.get(id=id_personal)
	if request.method == "GET":
		formulario = addPersonalForm(initial={
						'nombre':personal.nombre,
						'apellido_Paterno':personal.apellido_Paterno,
						'apellido_Materno':personal.apellido_Materno,
						'telefono':personal.telefono,
						'email':personal.email,
						})
		status_actualizar = "active"
		ctx = {'personal':personal ,'form':formulario,'status_actualizar':status_actualizar}
		return render_to_response('personal/editPersonal.html',ctx,context_instance=RequestContext(request))
	if request.method == "POST":
		info = "informacion"
		form = addPersonalForm(request.POST,request.FILES,instance=personal)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			info = "Se guardo satisfactoriamente"
			status_actualizar = "active"
			lista_personal = Personal.objects.filter(status=True)
			ctx={'lista_personal':lista_personal,'status_actualizar':status_actualizar}
			return render_to_response('personal/listPersonalDel.html',ctx,context_instance=RequestContext(request))

def view_delete_personal(request,id_personal):
	mensaje = "El registro se ha elliminado correctamente"
	personal = Personal.objects.filter(id=id_personal)
	personal.delete()
	status_eliminar = "active"
	ctx = {'mensaje':mensaje,'status_eliminar':status_eliminar}
	return render_to_response('personal/rmPersonal.html',context_instance=RequestContext(request))
	

def view_list_personal_delete(request):
	lista_personal = Personal.objects.filter(status=True)
	status_eliminar = "active"
	ctx={'lista_personal':lista_personal,'status_eliminar':status_eliminar}
	return render_to_response('personal/listPersonalDel.html',ctx,context_instance=RequestContext(request))
	

def view_list_personal_edit(request):
	lista_personal = Personal.objects.filter(status=True)
	status_actualizar = "active"
	ctx={'lista_personal':lista_personal,'status_actualizar':status_actualizar}
	return render_to_response('personal/listPersonalEdit.html',ctx,context_instance=RequestContext(request))
	

