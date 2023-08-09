from django.test import TestCase
from .forms import TopicForm, CommentForm


class testCreateTopic(TestCase):
    def test_title_required(self):
        form = TopicForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_user_not_manually_inputted(self):
        form = TopicForm()
        self.assertTrue(form.Meta.exclude, ['creator'])
