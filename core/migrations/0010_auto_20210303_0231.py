# Generated by Django 3.1.7 on 2021-03-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210303_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
