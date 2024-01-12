# Generated by Django 4.0.2 on 2024-01-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_message_reply_message_message_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_message', models.TextField()),
                ('created_at', models.DateTimeField(default='2024-01-01 00:00:00')),
            ],
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
        migrations.RemoveField(
            model_name='message',
            name='reply_message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default='2024-01-01 00:00:00'),
        ),
        migrations.AddField(
            model_name='adminreply',
            name='user_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.message'),
        ),
    ]