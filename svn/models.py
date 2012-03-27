from django.db import models

# Create your models here.

#A single folder to checkout in an SVN Repository with its destination folders
class SvnRepo(models.Model):
    svn_shortname = models.CharField(max_length=16) 	#Name to Refer to the Repository By
    svn_cofolder = models.CharField(max_length=32) 	#Target Folder
    svn_url = models.URLField(verify_exists=False) 	#Repo URL
    svn_active = models.BooleanField()		  	#Is It Actively being built?
    svn_presentrev = models.PositiveSmallIntegerField(blank=True,null=True)	#Saved Repo Version
    svn_uname = models.CharField(max_length=16,blank=True)		#SVN Username	(if needed)
    svn_pass = models.CharField(max_length=16,blank=True)		#SVN Password 	(if needed)
    def __unicode__(self):
        return self.svn_shortname
#Packages can be placed into categories & Tags
class SvnPkgTag(models.Model):
    pkg_tag_name = models.CharField(max_length=16)
class SvnPkgCat(models.Model):
    pkg_cat_name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.pkg_cat_name
#Packages are made up of SvnRepos and have categories
class SvnPkg(models.Model):
    pkg_shortname = models.CharField(max_length=8)	#Short Name Of Package 	(fex) [PHX]
    pkg_longname = models.CharField(max_length=32)	#Package's Long Name	(fex) [Phoenix Storms Model Pack]
    pkg_description = models.TextField()		#Package Description	(fex) [A very large and expansive model pack.
    pkg_repos = models.ManyToManyField(SvnRepo)		#Repositories that package is made of
    pkg_filename = models.CharField(max_length=8)	#If we wanted to, we can have diff names than the short name!
    pkg_homepage = models.URLField()			#Link to the package's homepage
    pkg_active = models.BooleanField()			#Are we packaging this still? (showing on site)
    pkg_size = models.FloatField()			#Package Size in MiB
    pkg_tag = models.ManyToManyField(SvnPkgTag)
    pkg_cat = models.ForeignKey(SvnPkgCat)
    def __unicode__(self):
        return self.pkg_shortname

