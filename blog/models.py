from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	class Meta:
		verbose_name_plural = "Categorias"
		ordering = ['id']
	def __str__(self):
		return self.title

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	author = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateField()
	published = models.BooleanField(default=True)
	class Meta:
		verbose_name_plural = "Publicaciones"
		ordering = ['id']
	def __str__(self):
		return self.title
