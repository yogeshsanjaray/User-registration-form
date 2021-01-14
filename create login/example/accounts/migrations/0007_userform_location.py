# Generated by Django 2.2 on 2021-01-12 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userform'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]