# Generated by Django 4.0.2 on 2024-01-07 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokenpurchase',
            name='token',
        ),
        migrations.RemoveField(
            model_name='tokenpurchase',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='user',
        ),
        migrations.DeleteModel(
            name='ICO',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
        migrations.DeleteModel(
            name='TokenPurchase',
        ),
        migrations.DeleteModel(
            name='UserWallet',
        ),
    ]
