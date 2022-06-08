from django.contrib import admin
from .models import Post
from .models import crudst, crudst1
# Register your models here.
admin.site.register(Post)
admin.site.register(crudst)
admin.site.register(crudst1)