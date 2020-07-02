from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
import requests

from api.models import *
import local

class InitProject(APIView):
    def get(self, request):
        return Response({
            'success': True,
            'Fase': [3,2,1]
        })