from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard_view,name="dashboard"),
    path('<slug:slug>/',topic_detail_view,name="topic_item"),
    path('categories/<int:pk>/',selected_category_view, name="category-view"),
    path('create/topic/',createTopic,name="create-topic"),
    path('update-topic/<slug:slug>/',updateTopic,name="update-topic"),
]
