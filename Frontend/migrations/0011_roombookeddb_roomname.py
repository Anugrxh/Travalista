# Generated by Django 4.2.4 on 2023-11-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0010_roombookeddb'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombookeddb',
            name='roomname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]