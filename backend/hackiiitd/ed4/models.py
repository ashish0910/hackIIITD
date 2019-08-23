# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def custom_directory_path(instance,filename):
	return 'files/returns/{}'.format(filename)	

def custom_directory_path2(instance,filename):
	return 'files/pdf/{}'.format(filename)	

class PostFile(models.Model):
	document = models.FileField(upload_to = custom_directory_path2, blank = True)
	class Meta:
		ordering = ["-id"]

	def __str__(self):
		return str(self.id)

class VidTextFile(models.Model):
	document = models.OneToOneField(PostFile, on_delete = models.CASCADE, primary_key=True)
	
	text = models.TextField(max_length = 2000,blank=True)

	video = models.FileField(upload_to=custom_directory_path, blank=True)

	def __str__(self):
		return str(self.document)