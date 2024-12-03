from django.shortcuts import render
from django.db.models import Count
from .models import Topic, Post
from django.views.generic import ListView, DetailView

def home(request):
    
    latest_posts = Post.objects.filter(status='published').order_by('-published')[:3]
    
    topics = (
        Topic.objects.annotate(post_count=Count('posts'))
        .order_by('-post_count')[:10]
    )
    context = {
        'latest_posts': latest_posts,
        'topics': topics,
    }
    return render(request, 'bpAp/home.html', context)

class TopicListView(ListView):
    model = Topic
    template_name = 'bpAp/topic_list.html'
    context_object_name = 'topics'
    ordering = ['name'] 

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'bpAp/topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            topics=self.get_object(),
            status='published'
        ).order_by('-published')  
        return context
  
    
class PostListView(ListView):
        model = Post
        context_object_name = 'posts'
        template_name = 'bpAp/post-list.html'
        queryset = Post.objects.filter(published__isnull=False).order_by('-published')


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset().filter(published__isnull=False)
        if 'pk' in self.kwargs:
            return queryset
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )