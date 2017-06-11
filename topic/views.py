from django.shortcuts import render

# Create your views here.

def home(request):
    template = 'topic/index.html'
    return render(request,template)