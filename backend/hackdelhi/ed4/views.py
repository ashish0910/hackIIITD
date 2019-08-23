from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .forms import *
from pdf_to_video import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, viewsets, routers

class PostFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostFile
        fields = ('document')

class PostFileSet(viewsets.ModelViewSet):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer

class VidTextFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VidTextFile
        fields = ('document','video','text')

class VidTextFileSet(viewsets.ModelViewSet):
    queryset = VidTextFile.objects.all()
    serializer_class = VidTextFileSerializer



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