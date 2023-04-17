from django.forms import ModelForm
from .models import Topic,Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ['creator','likes','topic_trending']
        
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

