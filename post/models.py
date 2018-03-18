from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

# Create your models here.
User = get_user_model()


class Topic(models.Model):
    topic_name = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_name

class Branch(models.Model):
    branch_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.branch_name


class Post(models.Model):
    user = models.ForeignKey(User ,blank=False)
    title = models.CharField(max_length=500 ,blank=False)
    content = models.TextField(blank=False )
    topic = models.ForeignKey(Topic)
    branch = models.ForeignKey(Branch)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('posts:single' ,kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']




class Comment(models.Model):
    post = models.ForeignKey(Post)










