from django.contrib import admin
from .models import Post

admin.site.disable_action('delete_selected')


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    actions = ['delete_selected']
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)