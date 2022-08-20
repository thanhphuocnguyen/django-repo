from django.contrib import admin

from .models import AccessRecord, Topic, WebPage

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)