from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/images")

    def __str__(self):
        return self.title

class Comment(models.Model):
    first_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)