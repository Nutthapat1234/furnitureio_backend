from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from helper import modifyRequest
from .models import ProductModel
from .serializer import ProductSerializer, ProductImageSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['productCode', 'name', 'price', 'furnitureType', 'brand', 'size', 'color', 'description']
    search_fields = ['name', 'brand', 'description']
    ordering_fields = ['price', 'size']

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        productCode = request.data['productCode']
        images = data.pop('image')
        detail = []

        try:
            productSerializer = ProductSerializer(data=modifyRequest(data))
            if productSerializer.is_valid():
                productSerializer.save()
                detail.append(productSerializer.data)
            for item in images:
                imageData = {'productCode': productCode, 'image': item}
                tempSerializer = ProductImageSerializer(data=imageData)
                if tempSerializer.is_valid():
                    tempSerializer.save()
                    detail.append(tempSerializer.data)
            return Response(detail, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

