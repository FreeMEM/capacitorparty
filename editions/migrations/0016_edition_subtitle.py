# Generated by Django 3.0.3 on 2020-05-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0015_auto_20200517_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
