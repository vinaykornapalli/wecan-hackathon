from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.conf import  settings
from django.utils.text import slugify
import  misaka as m
# Create your models here.
User = get_user_model()


class Topic(models.Model):
    topic_name = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_name

class Branch(models.Model):
    branch_name = models.CharField(max_length = 20)


class Post(models.Model):
    user = models.ForeignKey(User ,related_name='posts')
    slug = models.SlugField(user ,default="null")
    title = models.CharField(max_length=500 ,blank=False)
    content = models.TextField()
    topic = models.ForeignKey(Topic , related_name='posts')
    branch = models.ForeignKey(Branch,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('posts:single' ,kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','content']



class Comment(models.Model):
    post = models.ForeignKey(Post)










