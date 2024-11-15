from django.shortcuts import render
from django.db.models import Count
from .models import Topic, Post

def home(request):
    # Get the latest 3 published posts
    latest_posts = Post.objects.filter(status='published').order_by('-published')[:3]
    # Annotate topics with post counts and order by most popular topics
    topics = (
        Topic.objects.annotate(post_count=Count('posts'))
        .order_by('-post_count')[:10]
    )
    context = {
        'latest_posts': latest_posts,
        'topics': topics,
    }
    return render(request, 'bpAp/home.html', context)
