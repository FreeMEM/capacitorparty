# Generated by Django 3.0.7 on 2021-01-23 09:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0013_delete_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='videolink',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
