# Generated by Django 3.2 on 2021-04-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0029_alter_scener_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='scener',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scener',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]