# Generated by Django 2.2.5 on 2020-02-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200131_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.FloatField(),
        ),
    ]
