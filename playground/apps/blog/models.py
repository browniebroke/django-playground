from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed = False

    def __str__(self):
        return self.title
