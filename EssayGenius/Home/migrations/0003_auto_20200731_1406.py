# Generated by Django 2.2.5 on 2020-07-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200730_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='instructions',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]