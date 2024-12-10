from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app_1.forms import ProductoForm
from app_1.models import *
from django.http import JsonResponse,HttpResponse
from django.contrib import messages
@login_required
def productos(request):
    contexto = {}
    contexto['form_producto'] = ProductoForm()
    contexto['productos'] = Productos.objects.filter(activo=True)
    
    
    if request.POST:        
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
        else:
            print('form no valido')
            for field, error_list in form.errors.items():
                print(field,'¡¡¡¡',error_list)
    return render(request,'productos/productos.html',contexto)

def desactivar_producto(request,id_producto):
    try:
        producto = Productos.objects.get(id=id_producto)
        producto.activo = False
        producto.save()
        messages.success(request, 'Producto desactivado correctamente.')
        return redirect('productos')
    except Productos.DoesNotExist:
        return JsonResponse({"success": False, "message": "Producto no encontrado"})
    
def editar_producto(request,id_producto):
    print('editar producto')
    producto = Productos.objects.get(id=id_producto)
    print(producto)
    form_producto = ProductoForm(instance=producto)
    return render(request,'productos/modal_agregar_producto.html',{'form_producto':form_producto})
# def agregar_producto(request):
#     print('ENTRO AGREGAR PRODUCTO')
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('productos')
#     else:
#         form = ProductoForm()
#     return render(request, 'productos/agregar_producto.html', {'form': form})
    