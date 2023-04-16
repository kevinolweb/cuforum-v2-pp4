from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def dashboard_view(request):
    topic_activity=Topic.objects.all()
    context = {
        'topic_activity':topic_activity,
    }
    return render(request,'dashboard.html',context)
