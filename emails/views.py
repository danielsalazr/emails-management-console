from django.shortcuts import render

# Create your views here.
from  gmail import (
    gmail_authenticate,
    search_messages,
    read_message,
)

from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.parsers import MultiPartParser,FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

from rich.console import Console
console = Console()

@api_view(['GET'])
def getMails(request):
    pass

    # if data.exists():
    authentication = gmail_authenticate()

    messages = search_messages(authentication, "")[0:5]

    messageList = []

    for msg in messages:
        messageList.append(read_message(authentication, msg))

    # console.log(messages)
    console.log(messageList)
    return Response(messageList, status=status.HTTP_200_OK)
    # return Response({"res": "OK"}, status=status.HTTP_200_OK)

    # return Response('Not found', status=status.HTTP_404_NOT_FOUND)