# Generated by Django 3.2 on 2021-04-26 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0024_scener_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scener',
            name='external_link',
        ),
    ]
