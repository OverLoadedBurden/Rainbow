# Generated by Django 2.2.5 on 2020-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20200221_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(),
        ),
    ]
