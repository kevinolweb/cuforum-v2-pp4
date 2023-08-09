from django.test import TestCase
from .forms import TopicForm, CommentForm

class testCreateTopic(TestCase):
    def test_title_required(self):
        form = TopicForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'Field is required.')

    def test_summary_not_required(TestCase):
        form = TopicForm({'title': 'Test Title','slug':'test-title-xyz'})
        self.assertTrue(form.is_valid())

