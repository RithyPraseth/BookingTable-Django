# Generated by Django 5.1.2 on 2025-01-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_tblslide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblslide',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
