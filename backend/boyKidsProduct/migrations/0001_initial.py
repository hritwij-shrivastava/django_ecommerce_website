# Generated by Django 3.1.7 on 2021-03-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boyBrandTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=122)),
                ('brand_item_no', models.CharField(max_length=122)),
                ('brand_img', models.ImageField(upload_to='brand_logo')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='boyCategoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=122)),
                ('category_item_no', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BoyProductTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_unique_id', models.CharField(blank=True, max_length=122, null=True)),
                ('product_name', models.CharField(blank=True, max_length=122, null=True)),
                ('product_id', models.CharField(blank=True, max_length=122, null=True)),
                ('product_size', models.CharField(blank=True, max_length=122, null=True)),
                ('product_specification', models.CharField(blank=True, max_length=122, null=True)),
                ('product_color', models.TextField(blank=True, null=True)),
                ('product_img', models.ImageField(upload_to='product_images')),
                ('product_img_no', models.CharField(blank=True, max_length=122, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyKidsProduct.boybrandtable')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyKidsProduct.boycategorytable')),
            ],
        ),
        migrations.CreateModel(
            name='boyTagsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=122)),
                ('tags_no_item', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ImagesForBoyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_opt_img', models.ImageField(upload_to='product_images')),
                ('man_product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boyKidsProduct.boyproducttable')),
            ],
        ),
        migrations.AddField(
            model_name='boyproducttable',
            name='product_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyKidsProduct.boytagstable'),
        ),
    ]
