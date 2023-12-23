# Generated by Django 4.2.4 on 2023-11-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_hotelroomcatagorydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='roomdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(blank=True, max_length=25, null=True)),
                ('roomname', models.CharField(blank=True, max_length=25, null=True)),
                ('roomdescription', models.CharField(blank=True, max_length=125, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='room_image')),
            ],
        ),
    ]
