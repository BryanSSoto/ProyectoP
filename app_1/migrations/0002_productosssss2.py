# Generated by Django 3.2.12 on 2024-12-04 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productosssss2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productosssss', to='app_1.categorias')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productossssss', to='app_1.estados')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Productossss',
                'verbose_name_plural': 'Productosssss',
            },
        ),
    ]