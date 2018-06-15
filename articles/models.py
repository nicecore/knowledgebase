from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse(
            'articles:article-detail',
            kwargs={'slug': self.slug}
        )




class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
