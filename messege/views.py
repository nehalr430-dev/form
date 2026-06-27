from django.shortcuts import render
from .models import Message

# Create your views here.
def home(request):

    messages = Message.objects.all().order_by('-created_at')

    return render(request, 'messge/home.html', {'messages': messages})
