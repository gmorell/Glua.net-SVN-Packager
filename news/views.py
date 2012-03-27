# Create your views here.
from glua.news.models import *
from glua.svn.models import SvnPkg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
	addonlist = SvnPkg.objects.filter(pkg_active=1)
	newsitems  = Post.objects.order_by('-post_time')[0:3].all()
	title = "Index"
	pgjs = "index"
	#return render_to_response('news.html', {'newsitems': newsitems,'title':title,'pgjs':pgjs,'addonlist':addonlist,}, context_instance=RequestContext(request))
	return render_to_response('news.html', {'newsitems': newsitems,'title':title,'pgjs':pgjs,'addonlist':addonlist,})
def news(request, news_slug):
	item = Post.objects.filter(post_slug= news_slug).get()
	title = item.post_title
	pgjs = "newsitem"
	return render_to_response('newspost.html', {'item': item,'title':title,'pgjs':pgjs})
def about(request):
	title = "About"
	pgjs = "about"
	return render_to_response('about.html', {'title':title,'pgjs': pgjs,})
def donate(request):
	pgjs = "donate"
	return render_to_response('donate.html', {'pgjs': pgjs,})
def listnews(request):
	newsitems = Post.objects.order_by('-post_time')[0:10].all()
	pgjs = "newslist"
	return render_to_response('listnews.html', {'newsitems': newsitems, 'pgjs': pgjs,})
def legal(request):
	title = "Legal"
	pgjs = "legal"
	return render_to_response('legal.html', {'title':title,'pgjs': pgjs,})
	
