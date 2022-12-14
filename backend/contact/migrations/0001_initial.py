# Generated by Django 3.1.7 on 2021-03-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to='pages')),
                ('address', models.CharField(max_length=122)),
                ('phoneNo', models.CharField(max_length=122)),
                ('email_id', models.CharField(max_length=122)),
                ('workingHour1', models.CharField(max_length=122)),
                ('workingHour2', models.CharField(max_length=122)),
                ('facebook_url', models.CharField(max_length=122)),
                ('twitter_url', models.CharField(max_length=122)),
                ('insta_url', models.CharField(max_length=122)),
                ('linkedin_url', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='footerAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('url', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='footerCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('url', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='footerUsefulLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('url', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='userMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=122)),
                ('user_email', models.CharField(max_length=122)),
                ('user_msz', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
