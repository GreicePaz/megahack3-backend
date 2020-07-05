from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests
import json

from api.models import *
from api.utils import *
import local

class HelloWord(APIView):
    def get(self, request):
        return Response(True, status=status.HTTP_200_OK)


class OngAPI(APIView):
    def post(self, request):
        cnpj        = request.POST.get('cnpj')
        cep         = request.POST.get('cep')

        if not all([cnpj, cep]):
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            int(cep)
            int(cnpj)
        except:
            return Response({'success': False, 'detail':'Parâmetros incorretos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ong = Ong.objects.get(cnpj=cnpj)
        except: 
            ong = None

        if ong != None:
            return Response({'success': False, 'detail':'Ong já cadastrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = OngModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {'success': True, 'ong': serializer.data}

            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response({'success': False, 'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id == None:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ong = Ong.objects.get(id=id)
        except:
            return Response({'success': False, 'detail':'Id ong não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OngModelSerializer(ong)

        products = NeedProduct.objects.filter(ong=ong)
        bills = NeedBill.objects.filter(ong=ong)
        
        response = {'success': True, 'ong': serializer.data}
        response['ong'].update({'need_products': products, 'need_bills': bills})

        return Response(response)


class NeedProductAPI(APIView):
    def post(self, request):
        pass

    def get(self, request, id=None):
        if id == None:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            need = NeedProduct.objects.get(id=id)
        except:
            return Response({'success': False, 'detail':'Id necessidade não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NeedProductModelSerializer(need)

        response = {'success': True, 'need': serializer.data}

        return Response(response)


class NeedBillAPI(APIView):
    def post(self, request):
        pass

    def get(self, request, id=None):
        if id == None:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            need = NeedBill.objects.get(id=id)
        except:
            return Response({'success': False, 'detail':'Id necessidade não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NeedBillModelSerializer(need)

        response = {'success': True, 'need': serializer.data}

        return Response(response)


class TagAPI(APIView):
    def post(self, request):
        name = request.POST.get('name')

        if not name:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tag = Tag.objects.get(name=name)
        except: 
            tag = None

        if tag != None:
            return Response({'success': False, 'detail':'Tag já cadastrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TagModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {'success': True, 'tag': serializer.data}

            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response({'success': False, 'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            tags = Tag.objects.all()
        except:
            return Response({'success': False, 'detail':'Erro ao buscar tags'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TagModelSerializer(tags, many=True)

        response = {'success': True, 'tags': serializer.data}

        return Response(response)


class TagNeedProductAPI(APIView):
    def post(self, request):
        name = request.POST.get('name')

        if not name:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tag = Tag.objects.get(name=name)
        except: 
            tag = None

        if tag != None:
            return Response({'success': False, 'detail':'Tag já cadastrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TagModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {'success': True, 'tag': serializer.data}

            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response({'success': False, 'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            tags = Tag.objects.all()
        except:
            return Response({'success': False, 'detail':'Erro ao buscar tags'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TagModelSerializer(tags, many=True)

        response = {'success': True, 'tags': serializer.data}

        return Response(response)


class ProductsMeli(APIView):
    def get(self, request):
        search = request.GET.get('search')

        if not search:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        params = {'q': search}
        try:
            r = requests.get(local.URL_ML, params=params)
            result = r.json()
        except:
            return Response({'success': False, 'detail':'Erro na pesquisa'}, status=status.HTTP_404_NOT_FOUND)
        
        response = {'success': True, 'result': result}
        
        return Response(response)

