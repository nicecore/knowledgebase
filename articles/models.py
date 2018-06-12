from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
