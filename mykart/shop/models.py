from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    prod_name= models.CharField(max_length=50)
    prod_desc = models.CharField(max_length = 300)
    price = models.CharField(max_length=10,default = "")
    pub_date = models.DateField()
    category = models.CharField(max_length = 50,default ="")
    sub_category = models.CharField(max_length = 50,default ="")
    prod_image = models.ImageField(upload_to="shop/images",default ="")

    def __str__(self):
        return self.prod_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."