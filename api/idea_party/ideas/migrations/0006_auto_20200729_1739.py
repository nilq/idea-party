# Generated by Django 3.0.8 on 2020-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20200729_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published'),
        ),
    ]
