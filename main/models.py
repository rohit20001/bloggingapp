from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)