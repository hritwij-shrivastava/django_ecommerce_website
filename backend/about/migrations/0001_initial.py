# Generated by Django 3.1.7 on 2021-03-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutHeaderText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('desc', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='aboutSliderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sliderImage', models.ImageField(upload_to='pages')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='companyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.CharField(max_length=122)),
                ('title_data1', models.CharField(max_length=122)),
                ('data2', models.CharField(max_length=122)),
                ('title_data2', models.CharField(max_length=122)),
                ('data3', models.CharField(max_length=122)),
                ('title_data3', models.CharField(max_length=122)),
                ('data4', models.CharField(max_length=122)),
                ('title_data4', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderImage', models.ImageField(upload_to='pages')),
                ('leader_name', models.CharField(max_length=122)),
                ('leader_designation', models.CharField(max_length=122)),
                ('leader_desc', models.CharField(max_length=122)),
                ('leader_social_media', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visionImage', models.ImageField(upload_to='pages')),
                ('vision_desc', models.CharField(max_length=122)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
