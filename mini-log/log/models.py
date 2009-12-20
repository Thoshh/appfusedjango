from django.db import models

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    nick = models.CharField(max_length=20)
    comment = models.TextField()

