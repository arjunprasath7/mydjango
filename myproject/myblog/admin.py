from django.contrib import admin

from myblog.models import Posts, Comments

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 3


class PostsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['postTitle']}),
        (None,               {'fields': ['postData']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    inlines = [CommentsInline]

admin.site.register(Posts, PostsAdmin)


# Register your models here.
