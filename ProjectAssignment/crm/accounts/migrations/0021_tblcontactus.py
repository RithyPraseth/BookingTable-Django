# Generated by Django 5.1.2 on 2025-02-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_tbltopmenu_topmenulink'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('callUs', models.CharField(max_length=200, null=True)),
                ('emailUs', models.CharField(max_length=200, null=True)),
                ('openHour', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
