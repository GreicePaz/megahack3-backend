from api.models import *

from django.db import transaction


def insertProductsMeli(name, value, image, url):
    try:
        meli = ProductsMeli.objects.get_or_create(url=url)
    except:
        meli = None

    if meli != None:
        return False

    obj = meli.update(name=name, value=value, image=image)

    return obj.id

def insertTag(tags):
    try:
        tags = tags.split(",")
    except:
        pass

    for tag in tags:
        try:
            t = Tag.objects.get(name=tag)
        except:
            t = Tag.objects.create(name=tag)

    return True