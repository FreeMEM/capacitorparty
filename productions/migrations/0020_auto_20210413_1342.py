# Generated by Django 3.1.6 on 2021-04-13 11:42

from django.db import migrations, models
import upload_validator


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0019_auto_20210413_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='filepath',
            field=models.FileField(upload_to='files', validators=[upload_validator.FileTypeValidator(allowed_types=['application/x-amiga-disk-format'])]),
        ),
    ]
