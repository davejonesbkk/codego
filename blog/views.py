from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, Contact, ImageUpload
from taggit.models import Tag
from .forms import CommentForm, ContactForm



from django.core.mail import send_mail



def post_list(request):

	posts = Post.published.all()


	return render(request, 'blog_list.html', {'posts': posts})


def post_detail(request, slug):


	post = get_object_or_404(Post, slug=slug, status='published')

	comments = post.comments.filter(active=True)
	if request.method == 'POST':
		form = CommentForm(data=request.POST)

		if form.is_valid():
		
			new_comment = form.save(commit=False)
			new_comment.post = post 
			
			new_comment.save()


	else:
		form = CommentForm()


	return render(request, 'detail.html', {'post': post,
											'comments': comments,
											'form':form})



def tags_list(request, tag_slug=None):

	posts = Post.published.all()

	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		posts = posts.filter(tags__in=[tag])

	return render(request, 'tags_list.html', {'posts': posts})


def contact_form(request):

	sent = False

	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)

		if contact_form.is_valid():
			new_message = contact_form.save(commit=False)
			cd = contact_form.cleaned_data


			send_mail('New message!', cd['body'], cd['email'], ['dave.splashpress@gmail.com'])

			sent = True

			new_message.save()
			return HttpResponseRedirect('/thanks.html')

	else:
		contact_form = ContactForm()

	return render(request, 'contact.html', {'contact_form': contact_form,
											'sent': sent})


def thanks_page(request):

	return render(request, 'thanks.html')























