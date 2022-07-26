from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",
                              blank=True, upload_to="djangonautic/media/thumbs")
    # Add in thumbnail later
    # Add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]
