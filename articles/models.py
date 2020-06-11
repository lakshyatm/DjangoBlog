from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    likes = models.ManyToManyField(User, related_name="blog_posts",blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

# class Comment(models.Model):
#    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#    author = models.CharField(max_length=200)
#    text = models.TextField()
#    date = models.DateTimeField(auto_now_add=True)
#    approved_comment = models.BooleanField(default=False)
#
#    def approve(self):
#        self.approved_comment = True
#        self.save()

#    def __str__(self):
#        return self.text

#    def approved_comments(self):
#        return self.comments.filter(approved_comment=True)
