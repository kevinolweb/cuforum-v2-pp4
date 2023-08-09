from django.test import TestCase
from .models import Topic, Comment


class main_Views(TestCase):

    def testIndexPage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

    #check if non logged in user can access dashboard area
    def testDashboardPage_no_login(self):
        response=self.client.get('/dashboard/')
        self.assertEqual(response.status_code,301)
        self.assertTemplateUsed(response,'dashboard.html')

    def testCreateTopicPage(self):
        response=self.client.get('/create/topic')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'topic_create.html')