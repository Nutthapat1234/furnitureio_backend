from rest_framework import viewsets, status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from helper import modifyRequest
from .models import FurnitureSetModel
from products.serializer import ProductSerializer
from .serializer import FurnitureSetSerializers, FurnitureImageSerializer


# Create your views here.

class FurnitureSetView(viewsets.ModelViewSet):
    queryset = FurnitureSetModel.objects.all()
    serializer_class = FurnitureSetSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['furnitureSetCode']

    @action(methods=['get'], detail=True, url_path='items')
    def getItems(self, request, pk=None):
        queryset = self.queryset.filter(furnitureSetCode=pk)
        itemList = eval(queryset.values("itemList")[0]["itemList"])
        response = {}
        count = 1
        for code in itemList:
            try:
                response["item" + str(count)] = ProductSerializer.getProduct(code)[0].to_dict()
                count += 1
            except IndexError as e:
                print(e)

        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        furnitureSetCode = request.data['furnitureSetCode']
        images = data.pop('image')
        detail = []

        try:
            productSerializer = ProductSerializer(data=modifyRequest(data))
            if productSerializer.is_valid():
                productSerializer.save()
                detail.append(productSerializer.data)
            for item in images:
                imageData = {'furnitureSetCode': furnitureSetCode, 'image': item}
                tempSerializer = FurnitureImageSerializer(data=imageData)
                if tempSerializer.is_valid():
                    tempSerializer.save()
                    detail.append(tempSerializer.data)
            return Response(detail, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

