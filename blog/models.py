from django.db import models

class BlogPost(models.Model):
    title = models.TextField()
    context = models.TextField(null=True, blank=True)





