from rest_framework import serializers, status
from rest_framework.response import Response

from products.models import ProductModel, ProductImage
from furnitureIO.settings import URL
from helper import suggestProduct, createAccessURL


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'productCode', 'name', 'price', 'furnitureType', 'brand', 'size', 'color', 'description'
        )

    @staticmethod
    def getProduct(code):
        return ProductModel.objects.filter(productCode=code)

    def to_representation(self, instance):
        response = instance.to_dict()
        response['images'] = []
        for image in ProductImage.objects.filter(productCode=instance.productCode):
            response['images'].append(createAccessURL("furnitureio",'media/' + str(image)))
        if not response['images']:
            response['images'].append(createAccessURL("furnitureio",'media/None/no-image.jpg'))

        relateDetail = instance.to_dict()
        relateDetail.pop("productCode")
        relateDetail.pop("name")
        relateDetail.pop("description")
        suggestProduct(relateDetail, ProductModel.objects.filter)

        return response


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('productCode', 'image')
