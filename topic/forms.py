from django import forms

class TopicForm(forms.Form):
    topic = forms.CharField(label='Your Topics', max_length=255, widget=forms.Textarea(attrs={'class': 'form-control','rows': '2'}))