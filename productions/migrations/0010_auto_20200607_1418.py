# Generated by Django 3.0.3 on 2020-06-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0009_auto_20200607_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='production',
            name='videolink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
