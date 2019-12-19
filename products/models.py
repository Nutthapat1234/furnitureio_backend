from django.db import models


# Create your models here.
class ProductModel(models.Model):
    productCode = models.CharField(primary_key=True, max_length=10, null=False)
    name = models.TextField(null=False, default="")
    price = models.IntegerField(null=False, default=0)
    furnitureType = models.TextField(default=None)
    brand = models.TextField(default=None)
    size = models.TextField(default=None)
    color = models.TextField(default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.productCode

    def getCode(self):
        return self.productCode

    def to_dict(self):
        return {
            "productCode": self.productCode,
            "name": self.name,
            "price": self.price,
            "furnitureType": self.furnitureType,
            'size': self.size,
            "color": self.color,
            "description": self.description,
        }


class ProductImage(models.Model):
    auto_id = models.AutoField(primary_key=True)
    productCode = models.CharField(max_length=10, null=False)
    image = models.ImageField(upload_to="Images/Product/", default="Images/None/No-image.jpg")

    def __str__(self):
        return self.image.name