# Generated by Django 4.0.2 on 2024-01-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_link', models.URLField(blank=True, null=True, verbose_name='Instagram Link')),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='YouTube Link')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('telegram_link', models.URLField(blank=True, null=True, verbose_name='Telegram Link')),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Pages',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]