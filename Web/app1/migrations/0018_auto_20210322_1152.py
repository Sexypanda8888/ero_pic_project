# Generated by Django 3.1.6 on 2021-03-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20210308_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='img',
            name='md5',
            field=models.CharField(max_length=33, null=True),
        ),
        migrations.AddField(
            model_name='img',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]