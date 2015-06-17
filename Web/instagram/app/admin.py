from django.contrib import admin
from app.models import InstagramUser, Post, Comment, Follower, Like

class InstagramUserAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
class FollowerAdmin(admin.ModelAdmin):
    pass
class LikeAdmin(admin.ModelAdmin):
    pass

admin.site.register(InstagramUser, InstagramUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follower, FollowerAdmin)
admin.site.register(Like, LikeAdmin)

