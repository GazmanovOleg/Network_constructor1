from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Element_category)
admin.site.register(models.Router)
admin.site.register(models.Switch)
admin.site.register(models.Hub)
admin.site.register(models.Connections)
admin.site.register(models.End_devices)
admin.site.register(models.Element_list)
admin.site.register(models.Network_configuration)