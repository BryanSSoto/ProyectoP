from django.db import models
from django.contrib.auth.models import User

class ModeloBase(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class Categorias(models.Model):
    nombre = models.CharField(max_length=50,unique=True,help_text='Ingrese la categoria del Producto.')
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.nombre

class Productos(ModeloBase):
    class Estado(models.IntegerChoices):
        NUEVO = 1, 'Nuevo'
        SEMINUEVO = 2, 'Semi-nuevo'
        BUENESTADO = 3, 'Buen estado'
        USADO = 4, 'Usado'
        
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField(choices=Estado.choices,default=Estado.NUEVO)
    imagen = models.ImageField(upload_to='productos_imagenes/')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __str__(self):
        return ('%s, %s, %s' % (self.nombre,self.categoria,self.estado))
    