# Generated by Django 2.2.5 on 2020-08-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_uploadfiles_vueorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vueorders',
            name='style',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
