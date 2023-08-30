from django.contrib import admin
from .models import Location, Ad , VisitorCount , DailyLocationReport

# Register your models here.

admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(VisitorCount)
admin.site.register(DailyLocationReport)


