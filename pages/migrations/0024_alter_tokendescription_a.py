# Generated by Django 4.0.2 on 2024-01-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_tokendescription_delete_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokendescription',
            name='A',
            field=models.IntegerField(default=0),
        ),
    ]
