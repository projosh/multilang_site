from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title


