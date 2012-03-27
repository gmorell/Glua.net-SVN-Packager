import time
from glua.svn.models import *
from glua.balancer.models import *

from django.core.exceptions import ObjectDoesNotExist

def incfileday(fileobj):
	YMDObj = time.strftime("%Y,%m,%d").split(',')
	try:
		currentdata = Filetrackday.objects.filter(year=YMDObj[0]).filter(month=YMDObj[1]).filter(day=YMDObj[2]).filter(file=fileobj).get()
		currentdata.bandwidth += fileobj.pkg_size
		currentdata.dls += 1
		currentdata.save()
	except ObjectDoesNotExist:
		newdata = Filetrackday(year=YMDObj[0], month=YMDObj[1], day=YMDObj[2], bandwidth=fileobj.pkg_size, dls=1,file=fileobj)
		newdata.save()
	pass

def incfilemonth(fileobj):
	YMObj = time.strftime("%Y,%m").split(',')
	try:
                currentdata = Filetrack.objects.filter(year=YMObj[0]).filter(month=YMObj[1]).filter(file=fileobj).get()
                currentdata.bandwidth += fileobj.pkg_size
                currentdata.dls += 1
                currentdata.save()
        except ObjectDoesNotExist:
                newdata = Filetrack(year=YMObj[0], month=YMObj[1], bandwidth=fileobj.pkg_size, dls=1,file=fileobj)
                newdata.save()
        pass
def incbw(fileobj,mirrorobj):
	YMObj = time.strftime("%Y,%m").split(',')
	mirror = Mirrorbw.objects.filter(year=YMObj[0]).filter(month=YMObj[1]).get(mirror=mirrorobj)
	mirror.totalbw += fileobj.pkg_size
	mirror.save()
	

