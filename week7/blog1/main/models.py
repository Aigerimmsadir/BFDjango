from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     class Meta:
#         verbose_name = 'Author'
#         verbose_name_plural = 'Authors'

#     def __str__(self):
#         return "{} {}".format(self.first_name,self.last_name)


class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    content= models.TextField()
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return "{} {},{},{}".format(self.title,self.author, self.created,self.content )

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_of_author')
    created = models.DateTimeField(default = datetime.now())
    content= models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    def __str__(self):
        return "{} {},{},{}".format(self.author, self.created,self.content,self.post)
