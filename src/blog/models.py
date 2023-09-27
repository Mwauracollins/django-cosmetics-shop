from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=1200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    author = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = 'Post'
        verbose_name = 'Post'
        verbose_name_plural = 'Post'