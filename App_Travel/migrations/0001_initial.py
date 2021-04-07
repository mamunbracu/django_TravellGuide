# Generated by Django 3.0.3 on 2020-06-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
    ]