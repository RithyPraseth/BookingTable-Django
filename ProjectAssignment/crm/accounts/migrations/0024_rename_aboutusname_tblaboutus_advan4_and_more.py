# Generated by Django 5.1.2 on 2025-02-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_tblwhyus_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tblaboutus',
            old_name='aboutUsName',
            new_name='advan4',
        ),
        migrations.AddField(
            model_name='tblaboutus',
            name='introduction',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
