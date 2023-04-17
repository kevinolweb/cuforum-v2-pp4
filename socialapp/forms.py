from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Topic
from django.contrib.auth.models import User


class ForumUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        #fields = ['name', 'username', 'email', 'password1', 'password2']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ['creator']
        