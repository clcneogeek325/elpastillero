from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.pc.models import Pc
from apps.pc.forms import pcForm
from django.http import HttpResponseRedirect

def obtListaPCS():
	return Pc.objects.filter(status=True)


def view_addPc(request):
	if request.method == "POST":
		form = pcForm(request.POST)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.status = True
			edit.save()
			msg = "El registro %s de agrego corectamente" % edit.nombre_pc
			pcs = obtListaPCS()
			form = pcForm()
			ctx = {'form':form,'msg':msg,'lista_pc':pcs,'status_pc':'active'}
			return render_to_response('pc/addPc.html',ctx,
					context_instance=RequestContext(request))
		else:	
			pcs = obtListaPCS()
			form = pcForm()
			ctx = {'lista_pc':pcs,'form':form,'status_pc':'active'}
			return render_to_response('pc/addPc.html',ctx,
					context_instance=RequestContext(request))
		print "fue post"
	else:
		print "fue get"
		pcs = obtListaPCS()
		form = pcForm()
		ctx = {'lista_pc':pcs,'form':form,'status_pc':'active'}
		return render_to_response('pc/addPc.html',ctx,
				context_instance=RequestContext(request))
 
def view_editPc(request,id_pc):
	pc = Pc.objects.get(pk=id_pc)
	if request.method == "POST":
		print "fue post"
		form = pcForm(request.POST,instance=pc)
		if form.is_valid():
			form.save()
			form = pcForm(instance=pc)
			ctx = {'form':form}
			return HttpResponseRedirect('/addPC')
		else:
			pcs = obtListaPCS()
			form = pcForm()
			msg = "El formulario no es valido revisa vien por fabor"
			ctx = {'lista_pc':pcs,'form':form,'msg':msg,'status_pc':'active'}
			return render_to_response('pc/addPc.html',ctx,
					context_instance=RequestContext(request))
	else:
		print "fue get"
		form = pcForm(instance=pc)
		ctx = {'form':form,'status_pc':'active'}
		return render_to_response('pc/editPc.html',ctx,
				context_instance=RequestContext(request))

def view_rmPc(request,id_pc):
	pc = Pc.objects.get(pk=id_pc)
	if request.method == "POST":
		print "fue post"
		form = pcForm(request.POST,instance=pc)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.status = False
			edit.save()
			return HttpResponseRedirect('/addPC')
		else:
			pcs = obtListaPCS()
			form = pcForm()
			msg = "El formulario no es valido revisa vien por fabor"
			ctx = {'lista_pc':pcs,'form':form,'msg':msg,'status_pc':'active'}
			return render_to_response('pc/addPc.html',ctx,
					context_instance=RequestContext(request))
	else:
		print "fue get"
		form = pcForm(instance=pc)
		msg = "Esta usted seguro de querer dar de baja este registro"
		ctx = {'form':form,'status_pc':'active','msg':msg}
		return render_to_response('pc/rmPc.html',ctx,
				context_instance=RequestContext(request))




	
	
	
