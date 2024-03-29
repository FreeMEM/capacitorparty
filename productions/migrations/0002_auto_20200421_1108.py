# Generated by Django 3.0.3 on 2020-04-21 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='created_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='production',
            name='entry_author',
        ),
        migrations.AddField(
            model_name='production',
            name='classification',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='filepath',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productions.Files'),
        ),
        migrations.AlterField(
            model_name='production',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productions.ScenersGroup'),
        ),
    ]
