from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    descriptions = models.CharField(max_length=4999)
    publish_date = models.DateField()
    images = models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, default="")


    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=2000)
    amount = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    price = models.CharField(max_length=10, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:8] + "..."