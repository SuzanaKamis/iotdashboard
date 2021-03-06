# Generated by Django 3.0.4 on 2020-03-25 07:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('ipaddress', models.CharField(max_length=25)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sensorclient', serialize=False, to='home.Clients')),
                ('temperature', models.IntegerField(null=True)),
                ('luminosuty', models.IntegerField(null=True)),
                ('humidity', models.IntegerField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
