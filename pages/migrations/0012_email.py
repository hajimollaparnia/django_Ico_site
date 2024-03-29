# Generated by Django 4.0.2 on 2024-01-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_adminreply_sent_to_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=254)),
                ('to_email', models.EmailField(max_length=254)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
