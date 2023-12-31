# Generated by Django 4.2.4 on 2023-11-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutflightdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromplace', models.CharField(blank=True, max_length=50, null=True)),
                ('toplace', models.CharField(blank=True, max_length=50, null=True)),
                ('datefrom', models.IntegerField(blank=True, null=True)),
                ('dateto', models.IntegerField(blank=True, null=True)),
                ('travelclass', models.CharField(blank=True, max_length=50, null=True)),
                ('numpassengers', models.IntegerField(blank=True, null=True)),
                ('economyprice', models.IntegerField(blank=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('aadhar', models.IntegerField(blank=True, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('flightnumber', models.IntegerField(blank=True, null=True)),
                ('totalticketprice', models.IntegerField(blank=True, null=True)),
                ('flightname', models.CharField(blank=True, max_length=50, null=True)),
                ('pioletname', models.CharField(blank=True, max_length=50, null=True)),
                ('copioletname', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('totalseat', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
