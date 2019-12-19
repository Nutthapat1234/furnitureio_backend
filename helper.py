import random

from furnitureIO.settings import URL
from products.models import ProductModel
import boto3
from botocore.exceptions import ClientError
import requests

s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4', region_name='us-east-2'))


def modifyRequest(data):
    modified = {}
    for key, value in data.items():
        modified[key] = value[0]
    return modified


def createAccessURL(bName, oName, expiration=1000):
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bName,
                                                            'Key': oName},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        print(e)
        return None

    return response


def deleteObject(bName, oName):
    try:
        response = s3_client.delete_object(Bucket=bName, Key=oName)
    except ClientError as e:
        print(e)
        return None


def suggestProduct(fType, filter):
    filterStr = 'filter(furnitureType="' + fType + '")'
    items = eval(filterStr)
    itemURL = []
    print(items)
    if len(items) < 5:
        for i in items:
            itemURL.append("https://" + URL + "/api/v1/products/" + str(i))
    else:
        randomItems = random.choices(items, k=5)
        for i in randomItems:
            itemURL.append("https://" + URL + "/api/v1/products/" + str(i))
    return itemURL
