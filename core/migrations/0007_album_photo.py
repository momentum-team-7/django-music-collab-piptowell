# Generated by Django 3.1.7 on 2021-03-03 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_artist_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.ImageField(default=1, upload_to='albums'),
            preserve_default=False,
        ),
    ]