from django.test import TestCase
from .models import Topic, TopicCategory, Comment
from django.contrib.auth.models import User


class testTopicModel(TestCase):
    # test if topic can be created with trending set to false
    def test_create_topic_defaults_trending_false(self):
        new_user = User.objects.create_user('John Test 1990')
        cat = TopicCategory.objects.create(name="ICT")
        new_topic = Topic.objects.create(title='Test Topic Item',
                                         category_id=cat.id,
                                         creator_id=new_user.id)
        self.assertFalse(new_topic.topic_trending)

    # Tests max title characters is 250
    def test_title_max_chars(self):
        new_user2 = User.objects.create_user('Jane Test 1990')
        cat2 = TopicCategory.objects.create(name="Marketing")
        new_topic2 = Topic.objects.create(title='Test Topic Item 2',
                                          category_id=cat2.id,
                                          creator_id=new_user2.id)
        test_topic = Topic.objects.get(id=new_topic2.id)
        max_length = test_topic._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)