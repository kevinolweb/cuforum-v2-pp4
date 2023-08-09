from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Not createable for users
class CreditUnion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

# Not creatable for users
class TopicCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Topic Categories"

# Users discussion topics
class Topic(models.Model):
    category = models.ForeignKey(
        TopicCategory,
        related_name="categories",
        on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    summary = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)
    likes = models.ManyToManyField(User, related_name='topic_like', blank=True)
    topic_trending = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

#Users comments on each topic
class Comment(models.Model):
    commenter = models.EmailField()
    topic = models.ForeignKey(
        Topic,
        related_name="comments",
        on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:40]
