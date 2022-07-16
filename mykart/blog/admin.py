from django.contrib import admin
from .models import Blogpost

# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display = ('title','head0','pub_date')

admin.site.register(Blogpost, blogAdmin)