from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
import requests
import json

from api.models import *
import local

class HelloWord(APIView):
    def get(self, request):
        return Response(True)

class OngAPI(APIView):
    def post(self, request):
        name        = request.POST.get('name')
        cnpj        = request.POST.get('cnpj')
        description = request.POST.get('description')
        cep         = request.POST.get('cep')
        state       = request.POST.get('state')
        city        = request.POST.get('city')
        address     = request.POST.get('address')
        number      = request.POST.get('number')
        complement  = request.POST.get('complement', '')
        link        = request.POST.get('link', '')

        if not all([name, description, cep, state, address, number]):
            raise APIException('Parâmetros insuficientes', status_code=400)

        try:
            int(cep)
            int(number)
            int(cnpj)
        except:
            raise APIException('Parâmetros incorretos', status_code=400)

        try:
            ong = Ong.objects.get(cnpj=cnpj)
        except: 
            ong = None

        if ong not None:
            raise APIException('Ong já cadastrada', status_code=400)

        if len(cnpj) != 14:
            raise APIException('Parâmetros incorretos', status_code=400)

        params = {
            'name': name,
            'cnpj': cnpj,
            'description': description,
            'cep': cep,
            'state': state,
            'city': city,
            'address': address,
            'number': number,
            'complement': complement,
            'link': link
        }
        
        try:
            ong = Ong.objects.create(**params)
        except:
            raise APIException('Erro ao cadastrar', status_code=502)

        return Response(ong, status_code=201)