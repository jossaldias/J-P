# Generated by Django 4.2.1 on 2023-05-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='profile_default.png', upload_to='users/'),
        ),
    ]
