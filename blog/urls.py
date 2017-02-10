from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$', views.post_list, name='post_list'),
	url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.tags_list, name='post_list_by_tag'),
	url(r'^(?P<slug>[-\w+]+)$', views.post_detail, name='post_detail'),
	url(r'^contact.html', views.contact_form, name='contact_form'),
	url(r'^thanks.html', views.thanks_page, name='thanks_page'),
	url(r'^upload.html', views.ImageUpload, name='ImageUpload')
	

]