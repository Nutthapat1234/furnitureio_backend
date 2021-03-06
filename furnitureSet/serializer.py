from rest_framework import serializers
from .models import FurnitureSetModel, FurnitureImage
from furnitureIO.settings import URL
from helper import createAccessURL
import json


class FurnitureSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = FurnitureSetModel
        fields = ('furnitureSetCode', 'description', 'itemList', 'roomType', 'name', 'price')

    @staticmethod
    def getProduct(code):
        return FurnitureSetModel.objects.filter(productCode=code)[0]

    def to_internal_value(self, data):
        print(data.get("itemList"))
        itemList = json.dumps(data.get("itemList").split(","))
        validated = {
            "furnitureSetCode": data.get("furnitureSetCode"),
            "roomType": data.get("roomType"),
            "description": data.get("description"),
            "itemList": itemList
        }
        return validated

    def to_representation(self, instance):
        response = {
            "furnitureSetCode": instance.furnitureSetCode,
            "name": instance.name,
            "price": instance.price,
            "roomType": instance.roomType,
            "description": instance.description,
            "itemList": [],
            "images": []
        }
        for item in eval(instance.itemList):
            response['itemList'].append(item)

        for image in FurnitureImage.objects.filter(furnitureSetCode=instance.furnitureSetCode):
            response['images'].append(createAccessURL("furnitureio", 'media/' + str(image)))
        if not response['images']:
            response['images'].append(createAccessURL("furnitureio", 'media/None/no-image.jpg'))

        return response


class FurnitureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureImage
        fields = ('furnitureSetCode', 'image')

    @staticmethod
    def getProduct(code):
        return FurnitureImage.objects.filter(furnitureSetCode=code)
