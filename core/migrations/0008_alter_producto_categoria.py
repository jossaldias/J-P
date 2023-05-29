# Generated by Django 4.2.1 on 2023-05-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_producto_categoria_alter_producto_plataforma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('', '----'), ('Acción', 'Acción'), ('Aventura', 'Aventura'), ('Estrategia', 'Estrategia'), ('RPG', 'RPG'), ('Deportes', 'Deportes'), ('Música', 'Música'), ('Carreras', 'Carreras'), ('Puzzle', 'Puzzle'), ('Plataformas', 'Plataformas'), ('Shooter', 'Shooter'), ('Simulación', 'Simulación')], default='', max_length=200),
        ),
    ]
