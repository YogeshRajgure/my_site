from django.contrib import admin
from .models import Post, Author, Tag, Comments

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ("title", "date", "author")
    list_filter = ("author", "tags", "date")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, )
admin.site.register(Tag, )
admin.site.register(Comments, )