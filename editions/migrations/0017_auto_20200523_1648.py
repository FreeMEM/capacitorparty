# Generated by Django 3.0.3 on 2020-05-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0016_edition_subtitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edition',
            options={'ordering': ('-start',)},
        ),
        migrations.RemoveField(
            model_name='edition',
            name='pictures',
        ),
        migrations.DeleteModel(
            name='EditionPicture',
        ),
    ]
