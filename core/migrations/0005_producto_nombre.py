# Generated by Django 4.2.1 on 2023-05-19 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
