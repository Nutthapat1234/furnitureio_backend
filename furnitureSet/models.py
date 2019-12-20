from django.db import models


# Create your models here.
class FurnitureSetModel(models.Model):
    furnitureSetCode = models.CharField(primary_key=True, max_length=10, null=False)
    name = models.TextField(default="RoomSet I")
    price = models.IntegerField(default=0)
    roomType = models.TextField(default=None)
    description = models.TextField(default=None)
    itemList = models.TextField(default=None)

    def to_dict(self):
        return {
            'furnituresetCode': self.furnitureSetCode,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'roomType': self.roomType,
            'itemList': self.itemList
        }

    def getCode(self):
        return self.furnitureSetCode

class FurnitureImage(models.Model):
    auto_id = models.AutoField(primary_key=True)
    furnitureSetCode = models.CharField(max_length=10, null=False)
    image = models.ImageField(upload_to="Images/FurnitureSet/", default="Images/None/No-image.jpg")

    def __str__(self):
        return self.image.name
