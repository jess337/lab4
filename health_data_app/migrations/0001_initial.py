# Generated by Django 3.2.25 on 2024-10-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('blood_pressure', models.CharField(max_length=10)),
                ('cholesterol', models.FloatField()),
            ],
        ),
    ]
