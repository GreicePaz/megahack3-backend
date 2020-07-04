from django.urls import path

from api.views import *

urlpatterns = [
    path('', HelloWord.as_view()),
    path('ong/', OngAPI.as_view()),
    path('ong/<int:id>', OngAPI.as_view())
]
