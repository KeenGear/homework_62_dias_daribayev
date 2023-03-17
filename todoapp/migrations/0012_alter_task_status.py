# Generated by Django 4.1.6 on 2023-03-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_remove_task_project_task_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('New', 'new'), ('In Progress', 'in_progress'), ('Done', 'done')], default='todo', max_length=20),
        ),
    ]
