from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager 
from django_markdown.models import MarkdownField

#from django.utils.text import slugify


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=200)
	sub_heading = models.CharField(max_length=200, blank=True)
	slug = models.SlugField(max_length=200)
	body = models.TextField()
	image = models.ImageField(blank=False)
	author = models.ForeignKey(User, related_name='blog_posts')
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	

	tags = TaggableManager()

	objects = models.Manager()
	published = PublishedManager()


	class Meta:
		ordering = ('-created',)
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.slug])

class ImageUpload(models.Model):

	image_title = models.CharField(max_length=200)
	image_file = models.ImageField(blank=False, upload_to='media/')
	created = models.DateTimeField(default=None)

	class Meta:
		ordering = ('created', )

	def __str__(self):
		return self.image_title



class Comment(models.Model):

	post = models.ForeignKey(Post, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	

	class Meta:
		ordering = ('created', )
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)

class Contact(models.Model):


	name = models.CharField(max_length=200)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created', )
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'


	def __str__(self):
		return self.email
















