from django.contrib import admin
from .models import project_attraction,project,picture,city,attraction
# Register your models here.
#admin.site.register(Room)
#admin.site.register(Topic)
# 讓admin有資料庫
admin.site.register(project)
admin.site.register(project_attraction)
admin.site.register(picture)
admin.site.register(city)
admin.site.register(attraction)