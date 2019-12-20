from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from helper import modifyRequest, deleteObject
from .models import ProductModel
from .serializer import ProductSerializer, ProductImageSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['productCode', 'name', 'price', 'furnitureType', 'brand', 'size', 'color', 'description']
    search_fields = ['name', 'brand', 'description']
    ordering_fields = ['productCode', 'price', 'size']
    ordering = ['productCode']

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        productCode = request.data['productCode']
        images = data.pop('image')
        detail = []

        try:
            for item in images:
                imageData = {'productCode': productCode, 'image': item}
                tempSerializer = ProductImageSerializer(data=imageData)
                if tempSerializer.is_valid():
                    tempSerializer.save()
                    detail.append(tempSerializer.data)
            productSerializer = ProductSerializer(data=modifyRequest(data))
            if productSerializer.is_valid():
                productSerializer.save()
                detail.append(productSerializer.data)
            return Response(detail, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        code = request.data['productCode']
        try:
            product = ProductSerializer.getProduct(code)
            product.delete()
            product.save()

            productImages = ProductImageSerializer.getProduct(code)
            for image in productImages:
                deleteObject("furnitureio", 'media/' + str(image))
                image.delete()
                image.save()
            print("Delete Success")
            return Response([{"message": "Delete Product " + str(code)}], status=status.HTTP_200_OK)
        except:
            return Response([{"message": "Internal Error with Product " + str(code)}],
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
