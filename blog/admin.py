from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_diplay = ('id','title','slug')
	prepopulated_fields = {'slug':('title',)}
	list_filter = ['id']
	search_fields = ['title']
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
	list_diplay = ('id','title','slug','author','content','created_date','published_date','published')
	list_filter = ['id', 'created_date', 'published_date', 'published']
	search_fields = ['title','content']
	prepopulated_fields = {'slug':('title',)}
admin.site.register(Post, PostAdmin)