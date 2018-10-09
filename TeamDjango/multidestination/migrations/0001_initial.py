# Generated by Django 2.1.2 on 2018-10-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripHotelSearch',
            fields=[
                ('trip', models.AutoField(primary_key=True, serialize=False)),
                ('city_1', models.CharField(blank=True, max_length=100)),
                ('checkin_1', models.DateField()),
                ('checkout_1', models.DateField()),
                ('numberOfPersons_1', models.CharField(max_length=140)),
                ('city_2', models.CharField(blank=True, max_length=100)),
                ('checkin_2', models.DateField()),
                ('checkout_2', models.DateField()),
                ('numberOfPersons_2', models.CharField(max_length=140)),
                ('city_3', models.CharField(blank=True, max_length=100)),
                ('checkin_3', models.DateField()),
                ('checkout_3', models.DateField()),
                ('numberOfPersons_3', models.CharField(max_length=140)),
                ('budget', models.IntegerField()),
            ],
        ),
    ]
