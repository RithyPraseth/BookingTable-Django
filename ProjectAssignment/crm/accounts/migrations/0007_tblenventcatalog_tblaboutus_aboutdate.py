# Generated by Django 5.1.2 on 2025-01-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_productdate_tblfoodmenu_fooddate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblEnventCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogName', models.CharField(max_length=200, null=True)),
                ('catalogPrice', models.CharField(max_length=200, null=True)),
                ('catalogImage', models.ImageField(upload_to='CatalogImages/')),
                ('phoneNumber', models.CharField(max_length=15, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('catalogDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tblaboutus',
            name='aboutDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
