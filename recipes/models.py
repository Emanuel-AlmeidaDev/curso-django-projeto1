from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField('Título', max_length=65)
    description = models.CharField('Descrição', max_length=165)
    slug = models.SlugField('Slug')
    preparation_time = models.IntegerField('Tempo de preparo')
    preparation_time_unit = models.CharField('Unidade de Tempo', max_length=30)
    servings = models.IntegerField('Porções')
    servings_unit = models.CharField('Unidade de Porções', max_length=50)
    preparation_steps = models.TextField('Passos para a Preparação')
    preparation_steps_is_html = models.BooleanField(
        'Os passos de Preparação são HTML', default=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Criado em', auto_now=True)
    is_published = models.BooleanField('Foi publicado', default=False)
    cover = models.ImageField(
        'Imagem', upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
