# Generated by Django 3.0.3 on 2020-05-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0010_auto_20200517_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/media/'),
        ),
    ]
