from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app_1.forms import ProductoForm


@login_required
def productos(request):
    contexto = {}
    contexto['form_producto'] = ProductoForm()
    
    if request.POST:
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form no valido')
            for field, error_list in form.errors.items():
                print(field,'¡¡¡¡',error_list)
    return render(request,'productos/productos.html',contexto)

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
    