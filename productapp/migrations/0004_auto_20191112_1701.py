# Generated by Django 2.2.6 on 2019-11-12 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_auto_20191110_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='tot_qty1',
            new_name='tot_qty',
        ),
    ]