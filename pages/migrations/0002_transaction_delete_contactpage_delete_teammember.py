# Generated by Django 4.0.2 on 2024-01-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]