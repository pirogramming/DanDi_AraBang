# Generated by Django 2.2.9 on 2020-08-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_remove_school_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='gu',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='lat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='lng',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]