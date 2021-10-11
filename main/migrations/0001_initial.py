# Generated by Django 3.2.8 on 2021-10-09 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('price', models.BigIntegerField()),
                ('time', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=250)),
                ('discount', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('title', models.TextField()),
                ('telegram', models.CharField(max_length=250)),
                ('instagram', models.CharField(max_length=250)),
                ('facebook', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('number', models.CharField(max_length=250)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.courses')),
            ],
        ),
    ]
