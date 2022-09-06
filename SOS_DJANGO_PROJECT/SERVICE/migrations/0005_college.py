# Generated by Django 4.0.6 on 2022-08-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVICE', '0004_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(max_length=100)),
                ('collegeAddress', models.CharField(max_length=100)),
                ('collegeState', models.CharField(max_length=100)),
                ('collegeCity', models.CharField(max_length=100)),
                ('collegePhoneNumber', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'SOS_COLLAGE',
            },
        ),
    ]