# Generated by Django 4.0.2 on 2024-01-13 11:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_token_userwallet_tokenpurchase_smartcontract_ico'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
