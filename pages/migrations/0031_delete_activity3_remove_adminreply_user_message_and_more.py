# Generated by Django 4.0.2 on 2024-01-15 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_rename_activity1_roadmap1_rename_activity2_roadmap2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activity3',
        ),
        migrations.RemoveField(
            model_name='adminreply',
            name='user_message',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='AdminReply',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
