# Generated by Django 4.2.4 on 2023-08-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('pass_date', models.DateField()),
                ('adDateTime', models.DateTimeField()),
            ],
        ),
    ]
