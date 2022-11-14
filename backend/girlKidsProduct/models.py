from django.db import models

class girlCategoryTable(models.Model):
    category = models.CharField(max_length=122)
    category_item_no = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.category

class girlBrandTable(models.Model):
    brand = models.CharField(max_length=122)
    brand_item_no = models.CharField(max_length=122)
    brand_img = models.ImageField(upload_to="brand_logo")
    date = models.DateField()

    def __str__(self):
        return self.brand

class girlTagsTable(models.Model):
    tags = models.CharField(max_length=122)
    tags_no_item = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.tags

class GirlProductTable(models.Model):
    product_unique_id = models.CharField(max_length=122,blank=True, null=True)
    product_name = models.CharField(max_length=122,blank=True, null=True)
    product_id = models.CharField(max_length=122,blank=True, null=True)

    product_category = models.ForeignKey(girlCategoryTable,on_delete=models.CASCADE, blank=True, null=True)
    product_brand = models.ForeignKey(girlBrandTable,on_delete=models.CASCADE, blank=True, null=True)
    product_tag = models.ForeignKey(girlTagsTable,on_delete=models.CASCADE, blank=True, null=True)

    product_size = models.CharField(max_length=122, blank=True, null=True)
    product_specification = models.CharField(max_length=122, blank=True, null=True)
    product_color = models.TextField(blank=True, null=True)
    product_img = models.ImageField(upload_to="product_images")
    product_img_no = models.CharField(max_length=122,blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class ImagesForGirlProduct(models.Model):
    product_unique_id = models.CharField(max_length=122,blank=True, null=True)
    product_opt_img = models.ImageField(upload_to="product_images")
    woman_product_id = models.ForeignKey(GirlProductTable,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_unique_id
