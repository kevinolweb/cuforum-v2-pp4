from django.forms import ModelForm
from .models import Topic,Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ['creator']
        
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

