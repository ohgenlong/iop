from django.contrib import admin
from website.models import *

admin.site.register(TaskLog)
admin.site.register(TaskList)
admin.site.register(Host)
admin.site.register(Action)
admin.site.register(ServiceList)
admin.site.register(ServerStatus)
admin.site.register(UserProfile)
admin.site.register(Group)

# Register your models here.
