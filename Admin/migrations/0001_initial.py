# Generated by Django 2.2.5 on 2020-01-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('can_add', models.BooleanField()),
                ('can_delete', models.BooleanField()),
            ],
        ),
    ]
