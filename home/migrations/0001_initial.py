# Generated by Django 3.0.7 on 2021-08-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('msg', models.TextField()),
            ],
        ),
    ]
