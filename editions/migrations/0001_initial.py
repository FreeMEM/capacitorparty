# Generated by Django 3.0.3 on 2020-04-19 12:31

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'ordering': ('-modified_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-modified_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('published_productions', models.BooleanField(default=False)),
                ('place', tinymce.models.HTMLField()),
                ('description', models.ManyToManyField(to='productions.Description')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productions.Files')),
                ('organizers', models.ManyToManyField(to='productions.Scener')),
                ('sponsors', models.ManyToManyField(to='editions.Sponsors')),
            ],
            options={
                'ordering': ('-modified_at',),
                'abstract': False,
            },
        ),
    ]
