from django.contrib import admin

from .models import Template, User, Review
# Register your models here.

admin.site.register(Template)
admin.site.register(User)
admin.site.register(Review)