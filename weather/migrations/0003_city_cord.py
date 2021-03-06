# Generated by Django 2.2.2 on 2020-08-26 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20191119_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='City_cord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.City')),
            ],
        ),
    ]
