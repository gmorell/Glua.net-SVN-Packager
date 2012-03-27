from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostCategory(models.Model):
    category_name = models.CharField(max_length=64)
    category_desc = models.TextField()
    def __unicode__(self):
        return self.category_name
    
class Post(models.Model):
    post_title = models.CharField(max_length=64)
    post_category = models.ForeignKey(PostCategory)
    post_time = models.DateTimeField('Post Date')
    post_content = models.TextField()
    post_author = models.ForeignKey(User)
    post_slug = models.SlugField()
    def __unicode__(self):
        return self.post_title
