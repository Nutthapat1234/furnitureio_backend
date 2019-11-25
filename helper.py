from products.models import ProductModel


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
