# Generated by Django 3.0.3 on 2020-05-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0005_auto_20200421_1150'),
        ('editions', '0008_auto_20200516_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='productions',
            field=models.ManyToManyField(blank=True, to='productions.Production'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='editions.Sponsor'),
        ),
    ]