from django.contrib import admin
from .models import Track, LiteratureLinks, Choice, Question

# Register your models here.
admin.site.register(Track)
admin.site.register(LiteratureLinks)
admin.site.register(Choice)
admin.site.register(Question)