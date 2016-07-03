from django.contrib import admin
from .models import Ip, Switch, Switchport

class IpAdmin(admin.ModelAdmin):
    list_display = ['ip','hostname']
admin.site.register(Ip, IpAdmin)

class SwitchAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'ip', 'model']
admin.site.register(Switch, SwitchAdmin)


class SwitchportAdmin(admin.ModelAdmin):
    list_display = [ 'port', 'ip', 'duplex', 'speed', 'get_switch_hostname']

    def get_switch_hostname(self, obj):
        return obj.switch_hostname
    get_switch_hostname.admin_order_field = 'switch_hostname'
admin.site.register(Switchport, SwitchportAdmin)
