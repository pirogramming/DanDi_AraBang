# Generated by Django 2.2.9 on 2020-08-18 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='제목')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='All_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='all_post_photos')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='수정 시간')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment_like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='제목')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_list', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='post_photos')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='수정 시간')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.School')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
            ],
        ),
    ]
