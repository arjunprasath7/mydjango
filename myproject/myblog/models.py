from django.db import models


class Posts(models.Model):
	postTitle	=	models.CharField(max_length=200)
	postData	=	models.CharField(max_length=600)
	pub_date 	= 	models.DateTimeField('date published')
	def __str__(self):
		return self.postData


class Comments(models.Model):
	postId		=	models.ForeignKey(Posts)
	comments	=	models.CharField(max_length=300)
	commentDate	=	models.DateTimeField('date published')
	def __str__(self):
		return self.comments





# Create your models here.
