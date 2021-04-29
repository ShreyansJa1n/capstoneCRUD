# Generated by Django 3.0.5 on 2021-04-29 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dish',
            fields=[
                ('idF', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('ing', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('calories', models.FloatField()),
                ('typev', models.BooleanField()),
                ('chef', models.CharField(max_length=15)),
                ('dateAdded', models.DateField()),
                ('image', models.ImageField(upload_to='dishImages')),
            ],
        ),
        migrations.CreateModel(
            name='vegetables',
            fields=[
                ('idF', models.AutoField(primary_key=True, serialize=False)),
                ('vegename', models.CharField(max_length=15)),
                ('vegedish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restmanage.dish')),
            ],
        ),
    ]
