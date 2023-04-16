from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def dashboard_view(request):
    topic_activity=Topic.objects.all()
    categories_preview=TopicCategory.objects.all()
    context = {
        'topic_activity':topic_activity,
        'categories_preview':categories_preview,
    }
    return render(request,'dashboard.html',context)

def selected_category_view(request,pk):
    chosen_category=TopicCategory.objects.get(id=pk)
    category_topics=Topic.objects.filter(category=chosen_category)
    context = {
        'chosen_category':chosen_category,
        'category_topics':category_topics,
    }
    return render(request,'category_detail.html',context)

def topic_detail_view(request,slug):
    item=Topic.objects.get(slug=slug)
    categories_preview=TopicCategory.objects.all()
    context = {
        'item':item,
        'categories_preview':categories_preview,
    }
    return render(request,'topic_detail.html',context)