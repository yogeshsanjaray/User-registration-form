# Generated by Django 2.2 on 2021-01-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0002_auto_20210111_2058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserList',
        ),
    ]
