from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

   
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('topic_detail', args=[self.slug])

    def __str__(self):
        return self.name
   
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='draft') 
    published = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    topics = models.ManyToManyField(Topic, related_name='posts')


def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-detail', args=[self.slug])
        
def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

