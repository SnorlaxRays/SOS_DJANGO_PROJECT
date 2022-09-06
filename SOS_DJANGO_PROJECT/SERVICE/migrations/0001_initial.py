# Generated by Django 4.0.6 on 2022-07-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('login_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('confirmpassword', models.CharField(default='', max_length=20)),
                ('dob', models.DateField(max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('mobilenumber', models.CharField(default='', max_length=50)),
                ('role_Id', models.IntegerField()),
                ('role_Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SOS_USER',
            },
        ),
    ]
