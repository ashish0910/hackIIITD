from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

class PostFileView(APIView):
    def get(self, request):
        postfile = PostFile.objects.all()
        return Response({"postfile": postfile})

class VidTextFileView(APIView):
    def get(self, request):
        vidtextfile = VidTextFile.objects.all()
        return Response({"vidtextfile": vidtextfile})
