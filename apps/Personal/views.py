from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.Personal.forms import addPersonalForm
from apps.Personal.models import Personal
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from apps.Personal.forms import UserForm,ChangePasswdForm


def view_change_paswd(request,id_user):
	if request.user.is_authenticated() and request.user.is_staff:
		if request.method == "POST":
			form = ChangePasswdForm(request.POST)
			if form.is_valid():
				us = User.objects.get(pk=id_user)
				nueva_pass = form.cleaned_data['password']
				us.set_password(nueva_pass)
				us.save()
				msg = "La contrasenia se ha cambiado con exito"
				url = "/listPersonalEdit/"
				titulo = "Cambiando contrasenia"
				ctx = {'msg':msg,
					   'url':url,
					   'titulo':titulo}
				return render_to_response('personal/mensaje.html',ctx,context_instance=RequestContext(request))
		else:
			form = ChangePasswdForm()
			ctx = {'form':form}
		return render_to_response('personal/cambiarpasswd.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_add_personal(request):
	if request.user.is_authenticated() and request.user.is_staff:
		info = "informacion"
		if request.method == "POST":
			form_personal = addPersonalForm(request.POST)
			form_user = UserForm(request.POST)
			if form_personal.is_valid() and form_user.is_valid():
				addp = form_personal.save(commit=False)
				addp.status = True
				nombre_usuario = form_user.cleaned_data['user']
				contrasenia =  form_user.cleaned_data['password']
				correo = addp.email
				nombre = addp.nombre
				apellidos = "%s %s"%(addp.apellido_Paterno,addp.apellido_Materno)
				u = User.objects.create_user(username=nombre_usuario,email=correo,password=contrasenia)
				u.save()
				addp.user_id=u.id
				addp.save()
				usuario = User.objects.get(pk=u.id)
				usuario.first_name = nombre
				usuario.last_name = apellidos
				usuario.save()
				info = "Se guardo satisfactoriamente"
				status_agregar = "active"
				titulo = "Dal de alta a nuevos empleados"
				url = "/addPersonal/"
				ctx = {'status_agregar':status_agregar,
				'titulo':titulo,
				'url':url,
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
	else:
		return HttpResponseRedirect('/login')
		

def view_refresh_personal(request,id_personal):
	if request.user.is_authenticated() and request.user.is_staff:
		personal = Personal.objects.get(id=id_personal)
		if request.method == "GET":
			formulario = addPersonalForm(instance=personal)
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
				return render_to_response('personal/listPersonalEdit.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		

def view_delete_personal(request,id_personal):
	if request.user.is_authenticated() and request.user.is_staff:
		mensaje = "El registro se ha elliminado correctamente"
		personal = Personal.objects.get(id=id_personal)
		personal.status = False
		personal.save()
		u = User.objects.get(pk=personal.user_id)
		u.is_active = False
		u.save()
		status_eliminar = "active"
		ctx = {'mensaje':mensaje,'status_eliminar':status_eliminar}
		return render_to_response('personal/rmPersonal.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_list_personal_delete(request):
	if request.user.is_authenticated() and request.user.is_staff:
		lista_personal = Personal.objects.filter(status=True)
		status_eliminar = "active"
		ctx={'lista_personal':lista_personal,'status_eliminar':status_eliminar}
		return render_to_response('personal/listPersonalDel.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_list_personal_edit(request):
	if request.user.is_authenticated() and request.user.is_staff:
		lista_personal = Personal.objects.filter(status=True)
		status_actualizar = "active"
		ctx={'lista_personal':lista_personal,'status_actualizar':status_actualizar}
		return render_to_response('personal/listPersonalEdit.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

