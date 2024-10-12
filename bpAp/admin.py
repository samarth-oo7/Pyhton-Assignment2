from django.contrib import admin
from .models import Post,Comment,Topic


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'approved')  
    search_fields = ('name', 'email', 'text')  
    list_filter = ('approved',)  

    readonly_fields = ('name', 'email', 'text')  

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  
    readonly_fields = ('name', 'email', 'text')  
    can_delete = False  


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')  
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')  
    list_filter = ('status', 'topics')  

class TopicAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'slug')  


admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
