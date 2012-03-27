from glua.balancer.models import Files,Filetrack,Filetrackday,Mirror,Mirrorbw
from django.contrib import admin

class FileTrackAdmin(admin.ModelAdmin):
    #pass
    list_display = ('file','year','month','dls','bandwidth')
    list_filter = ('year','month','file')

class FileTrackDayAdmin(admin.ModelAdmin):
    #pass
    list_display = ('file','year','month','day','dls','bandwidth')
    list_filter = ('year','month','day','file')

class MirrorAdmin(admin.ModelAdmin):
    list_display = ('name','enabled','bwlimit','description')
    list_filter = ('enabled','bwlimit')

class MirrorBwAdmin(admin.ModelAdmin):
    list_display = ('mirror','year','month','totalbw')
    list_filter = ('mirror','month','year',)
    ordering = ('-year','month',)

admin.site.register(Files)
admin.site.register(Filetrack,FileTrackAdmin)
admin.site.register(Filetrackday,FileTrackDayAdmin)
admin.site.register(Mirror,MirrorAdmin)
admin.site.register(Mirrorbw,MirrorBwAdmin)