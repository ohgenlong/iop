from django.contrib import admin

from inv.models import *

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'phone')

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ServerCPU)
admin.site.register(ServerMemory)
admin.site.register(ServerHD)
admin.site.register(ServerRaidLevel)
admin.site.register(ServerRaidCard)
admin.site.register(ServerNIC)
admin.site.register(ServerAssetTemplate)
admin.site.register(ServerTemplateHDS)
admin.site.register(ServerTemplateNICS)
admin.site.register(SwitchAssetTemplate)
admin.site.register(ServerAsset)
admin.site.register(SwitchAsset)
