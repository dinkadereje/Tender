# Generated by Django 4.2.1 on 2023-05-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tender_publishedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
