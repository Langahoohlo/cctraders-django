from django.contrib import admin

from .models import ServiceOne, ServiceTwo, ServiceThree

class ServiceOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'serviceName', 'servicceDescription')
    list_display_links = ('id', 'serviceName')
    list_per_page = 25

class ServiceTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'serviceName', 'servicceDescription')
    list_display_links = ('id', 'serviceName')
    list_per_page = 25

class ServiceThreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'serviceName', 'servicceDescription')
    list_display_links = ('id', 'serviceName')
    list_per_page = 25

admin.site.register(ServiceOne, ServiceOneAdmin)
admin.site.register(ServiceTwo, ServiceTwoAdmin)
admin.site.register(ServiceThree, ServiceThreeAdmin)