# Generated by Django 2.2.5 on 2020-02-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0002_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='credit_card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='offer_at_the_time',
            field=models.FloatField(),
        ),
    ]
