# Generated by Django 3.1.7 on 2021-03-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menProduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesformenproduct',
            name='product_unique_id',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
