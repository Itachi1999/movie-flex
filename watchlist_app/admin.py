from django.contrib import admin
from watchlist_app.models import DigitalContent, StreamingPlatform

# Register your models here.
admin.site.register([DigitalContent, StreamingPlatform])
