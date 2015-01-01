from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from myblog.models import Posts,Comments
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime


def index(request):
	postsList 	= 	Posts.objects.order_by('-pub_date')[:5]
	context 	= 	{'postsList': postsList}
	return render(request, 'index.html', context)

def newPost(request):
	return render(request,'addform.html')

def createPost(request):
	title = request.POST['title']
	postData = request.POST['postData']
	createDate = datetime.now()
	create = Posts.objects.create(postTitle=title,postData=postData,pub_date=createDate)
	create.save()
	return render(request,'success.html')

def createComment(request):
	commentData=request.POST['commentData']
	postId=request.POST['postId']
	createDate = datetime.now()
	create = Comments.objects.create(comments=commentData,commentDate=createDate,postId_id=postId)
	create.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def detail(request,postId):
	postDetails = get_object_or_404(Posts, pk=postId)
	# comments = get_object_or_404(Comments, postId_id=postId)
	commentsAll = Comments.objects.filter(postId_id=postId) 
	return render(request, 'detail.html', {'postDetails': postDetails,'commentsData':commentsAll})
# Create your views here.
