# Generated by Django 5.2.2 on 2025-06-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapi', '0003_remove_worker_name_worker_user_alter_worker_worktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='subs',
            field=models.DateField(blank=True, null=True),
        ),
    ]
