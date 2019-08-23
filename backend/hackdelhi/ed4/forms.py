from django import forms
from .models import *


class PostFileForm(forms.ModelForm):
	class Meta:
		model = PostFile
		fields = ('document',)
		widgets = {
            'document': forms.FileInput()
        }