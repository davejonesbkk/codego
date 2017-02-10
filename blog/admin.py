from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin


from .models import Post, Comment, Contact, ImageUpload


class PostAdmin(MarkdownModelAdmin):

	list_display = ('title', 'slug', 'author', 'status', 'image')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['status', 'created']


class CommentAdmin(admin.ModelAdmin):

	list_display = ('name', 'email', 'post', 'created', 'active')

class ContactAdmin(admin.ModelAdmin):

	list_display = ('name', 'email', 'created')

class ImageUploadAdmin(admin.ModelAdmin):


	list_display = ('image_title', 'image_file')


admin.site.register(Post, MarkdownModelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ImageUpload, ImageUploadAdmin)








