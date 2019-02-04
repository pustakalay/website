# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.static import serve
from forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from joinImage import execute
from pdf2image import convert_from_path
import os.path
from django.http import HttpResponse

# Create your views here.

def index(request):
    BASE = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.abspath(os.path.join(BASE, '..'))
    folder = os.path.abspath(os.path.join(folder, 'media'))
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            fs = FileSystemStorage()
            i = 1
            for file in request.FILES.getlist('document'):
                filename = 'Test-' + str(i) + '-1.jpg'
                pdffilename = 'Test-' + str(i)
                if (".jpg" in file.name) or (".jpeg" in file.name):                     
                    fs.save(filename, file)
                if (".pdf" in file.name):
                    fs.save(file.name, file)
                    pdf_file_path = os.path.join(folder, file.name)
                    pages = convert_from_path(pdf_file_path, output_folder=folder, fmt='jpg', output_file=pdffilename)
                i = i + 1
            execute()
            filepath = os.path.join(folder, 'Result.jpg')
            return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
            return render(request, 'utility/index.html', {
        'form': form
    })
    else:
        form = DocumentForm()
    return render(request, 'utility/index.html', {
        'form': form
    })