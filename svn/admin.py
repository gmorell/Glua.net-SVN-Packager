from glua.svn.models import SvnRepo, SvnPkg, SvnPkgCat
from django.contrib import admin

class RepoAdmin(admin.ModelAdmin):
    list_filter = ('svn_active',)
    list_display = ('svn_shortname','svn_active','svn_presentrev')
    fieldsets = [
    (None,		{'fields': ['svn_shortname','svn_cofolder','svn_url','svn_active']}),
    ('Misc',		{'fields': ['svn_uname','svn_pass']}),
    ]
    
class PkgAdmin(admin.ModelAdmin):
    list_display = ('pkg_shortname','pkg_active')
    filter_horizontal = ('pkg_repos',)
    fieldsets = [
    (None,		{'fields': ['pkg_shortname','pkg_longname','pkg_repos','pkg_filename','pkg_active','pkg_cat']}),
    ('Datas',		{'fields': ['pkg_description','pkg_homepage','pkg_size']}),
    ]
admin.site.register(SvnRepo,RepoAdmin)
admin.site.register(SvnPkg,PkgAdmin)
admin.site.register(SvnPkgCat)
 
