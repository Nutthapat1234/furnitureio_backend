from rest_framework import serializers
from .models import FurnitureSetModel, FurnitureImage
from furnitureIO.settings import URL
import json


class FurnitureSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = FurnitureSetModel
        fields = ('furnitureSetCode', 'description', 'itemList')

    def to_internal_value(self, data):
        itemList = json.dumps(xdata.get("itemList").split(","))
        validated = {
            "furnitureSetCode": data.get("furnitureSetCode"),
            "description": data.get("description"),
            "itemList": itemList
        }
        return validated

    def to_representation(self, instance):
        response = {
            "furnitureSetCode": instance.furnitureSetCode,
            "description": instance.description,
            "itemList": [],
            "images": []
        }
        for item in eval(instance.itemList):
            response['itemList'].append(URL + 'api/v1/products/' + item)

        for image in FurnitureImage.objects.filter(furnitureSetCode=instance.furnitureSetCode):
            response['images'].append(URL + 'media/FurnitureSet' + str(image))
        if not response['images']:
            response['images'].append(URL + 'media/None/No-image.jpg')
        return response


class FurnitureImageSerializer(serializers.ModelSerializer):
    class MetaL:
        model = FurnitureImage
        fields = ('furnitureSetCode', 'image')
