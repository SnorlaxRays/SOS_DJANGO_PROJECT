# Generated by Django 4.0.6 on 2022-08-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVICE', '0008_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=20)),
                ('mobileNumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('college_ID', models.IntegerField()),
                ('collegeName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SOS_STUDENT',
            },
        ),
    ]
