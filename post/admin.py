from django.contrib import admin
from post.models import Branch , Topic , Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Branch)

