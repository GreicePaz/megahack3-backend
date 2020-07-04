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

    def get(self, request):
        id_ong = request.GET.get('id')

        if not id_ong:
            return Response({'success': False, 'detail':'Parâmetros insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ong = Ong.objects.get(id=id_ong)
        except:
            return Response({'success': False, 'detail':'Id ong não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OngModelSerializer(ong)

        response = {'success': True, 'ong': serializer.data}

        return Response(response)