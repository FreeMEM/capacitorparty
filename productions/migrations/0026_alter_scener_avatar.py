# Generated by Django 3.2 on 2021-04-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0025_remove_scener_external_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scener',
            name='avatar',
            field=models.ImageField(blank=True, height_field=60, null=True, upload_to='avatars', width_field=60),
        ),
    ]
