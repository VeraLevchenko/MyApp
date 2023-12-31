# Generated by Django 4.2.3 on 2023-07-09 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('inn', models.IntegerField()),
                ('type_subject', models.CharField(choices=[(0, 'физлицо'), (1, 'юрлицо')], max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('data', models.DateField()),
                ('info', models.TextField(max_length=254)),
                ('doc', models.FileField(upload_to='')),
                ('author', models.CharField(max_length=254)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.subject')),
            ],
        ),
    ]
