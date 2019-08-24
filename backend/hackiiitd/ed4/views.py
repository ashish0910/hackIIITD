from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponseRedirect
from pdf_to_video import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, viewsets, routers, permissions
import os
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.core.files import File
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AllowAll(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        return True        

        
class SaveTxtFile(APIView):
    permission_classes = [AllowAll]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        text = request.data.get('txt_string')
        count = PostFile.objects.count()
        print(text)
        print('*'*100)
        file = open("ed4/static/files/api_files/{}.txt".format(str(count)), "w")
        file.write(text)
        file.close()
        file = open("ed4/static/files/api_files/{}.txt".format(str(count)), 'r')
        post = PostFile.objects.create(document = File(file))
        try : 
            get_file_name(post.document.url,post)
        except Exception, e : 
            return Response({"response" : "error", "message" : str(e)})
        os.remove("ed4/static/files/api_files/{}.txt".format(str(count)))
        file.close()
        postfile = PostFile.objects.all()
        videoFiles = []
        pdfs = []
        i=0
        for obj in postfile:
            try:
                videoFiles.append(VidTextFile.objects.get(document=obj))
                pdfs.append(obj)
                i += 1
            except:
                pass
        form = PostFileForm()
        return render(request,'ed4/home.html',{'form': form, 'pdfs_and_videos' : zip(range(1,i+1),pdfs,videoFiles)})
        return Response({"response" : "success", "message" : "File Created Succesfully ! "})  

def HomeView(request):
    postfile = PostFile.objects.all()
    videoFiles = []
    pdfs = []
    i=0
    for obj in postfile:
        try:
            videoFiles.append(VidTextFile.objects.get(document=obj))
            pdfs.append(obj)
            i += 1
        except:
            pass
    if request.method == "POST":
        form = PostFileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            get_file_name(post.document.url,post)
            return redirect('home')
    else:
        form = PostFileForm()

    return render(request,'ed4/home.html',{'form': form, 'pdfs_and_videos' : zip(range(1,i+1),pdfs,videoFiles)})


def TestView(request):
    return render(request, 'ed4/testing.html')
