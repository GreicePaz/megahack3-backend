from api.models import *


def insertProductsMeli(name, value, image, url):
    try:
        meli = ProductsMeli.objects.get_or_create(url=url)
    except:
        meli = None

    if meli != None:
        return False

    obj = meli.update(name=name, value=value, image=image)

    return obj.id

def insertTags(tag, need, id_need):
    pass