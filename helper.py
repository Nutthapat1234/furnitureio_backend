from products.models import ProductModel
import boto3
from botocore.exceptions import ClientError


def modifyRequest(data):
    modified = {}
    for key, value in data.items():
        modified[key] = value[0]
    return modified


def suggestProduct(product, filter):
    relateItem = set()
    for key, value in product.items():
        filterStr = 'filter(' + key + '="' + str(value) + '")'
        if key == 'price':
            filterStr = "filter(price__range=(" + str(value - 500) + "," + str(value + 500) + "))"

        relateItem.add(eval(filterStr))

    print(relateItem)


def createAccessURL(bName, oName, expiration=1000):
    s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4', region_name='us-east-2'))
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bName,
                                                            'Key': oName},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        print(e)
        return None

    return response


