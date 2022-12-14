# Generated by Django 4.0.6 on 2022-08-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVICE', '0010_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examTime', models.CharField(max_length=40)),
                ('examDate', models.DateField()),
                ('subject_ID', models.IntegerField()),
                ('subjectName', models.CharField(max_length=50)),
                ('course_ID', models.IntegerField()),
                ('courseName', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SOS_TIMETABLE',
            },
        ),
    ]
