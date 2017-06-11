from django.shortcuts import render
from .forms import TopicForm

# Create your views here.

def home(request):
    template = 'topic/index.html'
    form = TopicForm()
    context = {
        'form':form
    }
    return render(request,template,context)