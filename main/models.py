from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class articles_de_blog(models.Model):
    title = models.CharField(max_length= 200, verbose_name=_("title"))
    content = models.TextField(verbose_name=_("content"))
    publication_date = models.DateTimeField(verbose_name=_("publication date"))

def __str__(self):
    return self.title
    





