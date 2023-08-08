from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import TopicForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    credit_unions=CreditUnion.objects.all()
    context = {
        'credit_unions':credit_unions,
    }
    return render(request,'index.html',context)

@login_required(login_url='/')
def dashboard_view(request):
    topic_activity=Topic.objects.all()
    categories_preview=TopicCategory.objects.all()
    context = {
        'topic_activity':topic_activity,
        'categories_preview':categories_preview,
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='/')
def selected_category_view(request,pk):
    chosen_category=TopicCategory.objects.get(id=pk)
    category_topics=Topic.objects.filter(category=chosen_category)
    context = {
        'chosen_category':chosen_category,
        'category_topics':category_topics,
    }
    return render(request,'category_detail.html',context)

@login_required(login_url='/')
def topic_detail_view(request,slug):
    item=Topic.objects.get(slug=slug)
    categories_preview=TopicCategory.objects.all()
    if request.method=='POST':
        new_comment=CommentForm(request.POST)
        if new_comment.is_valid():
            comm=new_comment.save(commit=False)
            comm.topic=item
            comm.commenter=request.user.username
            comm.save()
            messages.add_message(request, messages.SUCCESS,"Your comment was posted!")
            return redirect('dashboard')
        else:
            messages.error(request, 'Oops! There was an error and your comment could not be posted!')
    new_comment=CommentForm()
    context = {
        'item':item,
        'categories_preview':categories_preview,
        'new_comment':new_comment,
    }
    return render(request,'topic_detail.html',context)

@login_required(login_url='/')
def createTopic(request):
    if request.method=='POST':
        new_topic_form=TopicForm(request.POST)
        if new_topic_form.is_valid():
            obj=new_topic_form.save(commit=False)
            obj.creator=request.user
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Your topic was successfully created!')
            return redirect('dashboard')
        else:
            messages.error(request, 'This topic could not be created. This slug may already be in use please create a new one or create a ticket if you have further issues.')

    new_topic_form=TopicForm()
    context={
        'new_topic_form':new_topic_form,
    }
    return render(request,'topic_create.html',context)

@login_required(login_url='/')
def updateTopic(request,slug):
    topic=Topic.objects.get(slug=slug)
    selected_topic=TopicForm(instance=topic)
    if request.user != topic.creator:
        return HttpResponse('Your are not allowed here!')
    if request.method=='POST':
        selected_topic=TopicForm(request.POST,instance=topic)
        if selected_topic.is_valid():
            selected_topic.save()
            messages.add_message(request, messages.SUCCESS, 'Your topic was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Oops! Your topic could not be updated. Please ensure the slug is unique as it may already be in use. Please submit a ticket if further issues.')
    context={
        'selected_topic':selected_topic,
    }
    return render(request,'topic_update.html',context)

@login_required(login_url='/')
def deleteTopic(request,slug):
    topic=Topic.objects.get(slug=slug)
    if request.user != topic.creator:
        return HttpResponse('Your are not allowed here!')
    if request.method=='POST':
        topic.delete()
        messages.add_message(request, messages.INFO, 'Your topic was successfully deleted!')
        return redirect('dashboard')
    context={
        'topic':topic,
    }
    return render(request,'topic_delete.html',context)