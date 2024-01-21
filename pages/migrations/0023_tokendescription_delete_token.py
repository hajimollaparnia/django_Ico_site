# Generated by Django 4.0.2 on 2024-01-14 06:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_remove_smartcontract_token_delete_tokendescription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('a', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('B', models.TextField()),
                ('b', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('C', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('c', models.TextField(blank=True, null=True)),
                ('D', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('d', models.TextField(blank=True, null=True)),
                ('description1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('join_us_link', models.URLField(blank=True, null=True)),
                ('buy_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]