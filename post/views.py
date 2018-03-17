from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from . import  models
from . import forms
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin


User = get_user_model()

class PostListAll(generic.ListView,SelectRelatedMixin):
    model = models.Post
    select_related = ('user','topic' , 'branch')


class PostListBranchWise(generic.ListView,SelectRelatedMixin):
    model = models.Post
    select_related = ('user','branch')



class PostListTopicWise(generic.ListView,SelectRelatedMixin):
    model = models.Post
    select_related = ('user','topic')



class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list'
    def get_quertset(self):
        try:
           self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context




class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','branch','topic')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))



    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))



class CreatePost(generic.CreateView,SelectRelatedMixin,LoginRequiredMixin):
    fields = ('content','branch','topic')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class DeletePost(generic.DeleteView,LoginRequiredMixin):
    model = models.Post
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, request, *args, **kwargs):
        return super().delete(*args,**kwargs)




