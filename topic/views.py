from django.shortcuts import render, redirect, HttpResponse
from .forms import TopicForm
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def vote(request):
    if request.method == 'POST':
        voted_topic_id = int(request.POST.get("id"))
        vote_type = request.POST.get("type")
        voted_topic_index = next(index for (index, d) in enumerate(topic_list) if d["id"] == voted_topic_id)
        if vote_type =="positive":
            topic_list[voted_topic_index]['votes']+=1
        elif vote_type =="negative":
            topic_list[voted_topic_index]['votes']-=1
        else:
            return HttpResponse('error-unknown vote type')
        voted_topic_votes = topic_list[voted_topic_index]['votes']
        return HttpResponse(voted_topic_votes)