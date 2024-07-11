# FixedAssets_BE/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'project_name': 'Fixed Asset Management'})
