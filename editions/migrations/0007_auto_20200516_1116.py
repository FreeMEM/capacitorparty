# Generated by Django 3.0.3 on 2020-05-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0006_auto_20200513_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='sponsors',
            field=models.ManyToManyField(to='editions.Sponsor'),
        ),
    ]
