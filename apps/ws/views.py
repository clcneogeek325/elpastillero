from django.http  import HttpResponse
from django.core import serializers
from apps.productos.models import Producto
from apps.proveedores.models import Proveedores
from apps.mercancia.models import Mercancia


def ws_buscar_producto(request,dato):
        info = serializers.serialize("json",Producto.objects.filter(nombre_producto__startswith=dato)[:5])
        return HttpResponse(info,mimetype="application/json")

def ws_buscar_proveedor_de_compania(request,id):
        info = serializers.serialize("json",Proveedores.objects.filter(compania_id=id))
        return HttpResponse(info,mimetype="application/json")


def ws_producto(request,id):
        info = serializers.serialize("json",Producto.objects.filter(pk=id))
        return HttpResponse(info,mimetype="application/json")

def ws_ultimos_registros(request):
        info = serializers.serialize("json",Mercancia.objects.all().order_by("id").reverse()[:5])
        return HttpResponse(info,mimetype="application/json")

