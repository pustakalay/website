'''
Created on 27-Jan-2019

@author: Tanay
'''
from django import forms
from models import Document

class DocumentForm(forms.ModelForm):
   class Meta:
        model = Document
        fields = ('document', )