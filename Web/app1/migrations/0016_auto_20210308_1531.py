# Generated by Django 3.1.6 on 2021-03-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20210308_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
