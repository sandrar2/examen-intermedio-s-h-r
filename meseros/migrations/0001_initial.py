# Generated by Django 4.2.7 on 2023-11-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meseros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('edad', models.IntegerField(default='00')),
                ('nacionalidad', models.CharField(default='', max_length=27)),
            ],
        ),
    ]
