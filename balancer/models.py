# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from glua.svn.models import SvnPkg

class Files(models.Model):
    id = models.IntegerField(primary_key=True)
    shortname = models.CharField(max_length=72)
    desc = models.TextField()
    livename = models.TextField()
    class Meta:
        db_table = u'files'
    def __unicode__(self):
        return self.desc

class Filetrack(models.Model):
    id = models.IntegerField(primary_key=True)
    month = models.IntegerField()
    year = models.IntegerField()
    bandwidth = models.IntegerField()
    file = models.ForeignKey(SvnPkg)
    dls = models.IntegerField()
    class Meta:
        db_table = u'filetrack'
    def __unicode__(self):
	return self.file.livename
    

class Filetrackday(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    bandwidth = models.IntegerField()
    file = models.ForeignKey(SvnPkg)
    dls = models.IntegerField()
    class Meta:
        db_table = u'filetrackday'
    def __unicode__(self):
        return self.file.desc

class Mirror(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    urlbase = models.TextField()
    bwlimit = models.IntegerField()
    description = models.TextField()
    enabled = models.BooleanField()
    url = models.TextField()
    class Meta:
        db_table = u'list'
    def __unicode__(self):
        return self.name
    
class Mirrorbw(models.Model):
    id = models.IntegerField(primary_key=True)
    month = models.IntegerField()
    year = models.IntegerField()
    mirror = models.ForeignKey(Mirror)
    totalbw = models.IntegerField()
    class Meta:
        db_table = u'mirrorbw'
    def __unicode__(self):
        return self.mirror.name

