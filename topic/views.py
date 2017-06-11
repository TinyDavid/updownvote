from django.shortcuts import render, redirect
from .forms import TopicForm
from operator import itemgetter
# Create your views here.

topic_list = list() # global variable topic list to store all post topics
topic_id = 0 # initial topic id =0, increament 1 with each post

def home(request):
    global topic_list,topic_id # set the variable to be global
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            topic = dict() #topic dictionary to store each topic with topic content, votes and id
            topic['topic'] = request.POST.get("topic")
            topic['votes'] = 0
            topic['id'] = topic_id
            topic_id+=1
            topic_list.append(topic)

    return redirect('/topic')

def topic(request):
    template = 'topic/index.html'  
    form = TopicForm()
    context = {
        'topic_list':topic_list,
        'form':form
    }
    return render(request,template,context)