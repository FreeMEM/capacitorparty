# Generated by Django 3.0.7 on 2021-01-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0014_auto_20210123_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='scener',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scenersgroup',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]