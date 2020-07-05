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

def createGetTag(tag):
    try:
        tag = Tag.objects.get_or_create(nome=name)
    except:
        return False

    return tag

def insertTag(tag, id, need_type):
    if need_type == 'cause':
        try:
            ong = Ong.objects.get(id=id)
        except:
            return False

        ong.tags.clear()
        


    