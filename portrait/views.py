from django.shortcuts import render, redirect
from generator import generate, generate_color
# Create your views here.

def index(request):
    context = {}
    #if(generate("model/g_[1400].h5","uploads/grayscale") and generate("model/g_[2000].h5","uploads/colored")):
    if(generate_color()):
        return render(request, 'index.html', context)
