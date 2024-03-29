# Generated by Django 2.2.1 on 2019-07-11 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
                ('presentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Presentation')),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=255)),
                ('organization', models.CharField(max_length=128)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Event')),
            ],
        ),
    ]
