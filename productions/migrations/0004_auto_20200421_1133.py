# Generated by Django 3.0.3 on 2020-04-21 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_auto_20200421_1133'),
        ('productions', '0003_auto_20200421_1124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]