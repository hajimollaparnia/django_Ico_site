# Generated by Django 4.0.2 on 2024-01-10 05:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_transaction_delete_contactpage_delete_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='About1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]