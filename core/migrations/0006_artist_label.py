# Generated by Django 3.1.7 on 2021-03-03 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_artist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='label',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
