# Generated by Django 3.0.3 on 2020-05-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0014_auto_20200517_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editionpicture',
            name='edition',
        ),
        migrations.AddField(
            model_name='edition',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='editions.EditionPicture'),
        ),
    ]
