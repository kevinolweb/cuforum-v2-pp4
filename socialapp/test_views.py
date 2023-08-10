from django.test import TestCase
from .models import Topic, Comment, TopicCategory
from django.test.client import Client
from django.shortcuts import redirect, reverse


class main_Views(TestCase):

    # check if index page is showing with no errors
    def testIndexPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # check if non logged in users are prevented from dashboard area
    def test_dashboard_redirect(self):
        response = self.client.get('/dashboard/')
        self.assertTrue(302, response.status_code)

    # check if sign in page loads
    def test_sign_in_page_loads(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
