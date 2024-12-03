from .models import Topic

def base_context(request):
    return {
        'top_topics': Topic.objects.all().order_by('name')[:5]  
    }