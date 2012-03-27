# Create your views here.
import time

from glua.svn.models import *
from glua.balancer.models import *
from glua.balancer.counts import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

from datetime import datetime
import random

#the index function is the download page function. We Grab the lowest 3 mirrors and pick one randomly :) FFFFUUUU Synergy
def standard(request,fileid):
	#something regarding the session and UPDATECOUNT=FALSE goes here.
	#get the current datetime
	date = datetime.now()
	#select threee lowest mirrors based on our current dealio
	lowestthree = Mirrorbw.objects.filter(year=date.year).filter(month=date.month).filter(mirror__enabled=1).order_by('totalbw')[0:3]
	#check that our queryset isn't empty, if it is, set it to mirror1 and then create the various numbers :<
	if lowestthree.count() == 0:
		mirrorid = 1 # pick our defacto mirror
		#lets setup our mirror bw counts for the next time.
		mirrorlist = Mirror.objects.all()
		for mirrord in mirrorlist:
			bwitem = Mirrorbw(year=date.year, month=date.month,mirror=mirrord,totalbw=0)
			bwitem.save()
			
	else:
		ids = list()
		for low in lowestthree:
			ids.append(low.mirror.id)
		mirrorid = random.sample(ids,1)[0]
		#mirrorid = lowestthree.order_by('?')[0].mirror.id # else pick one of the random ones
	#get the file info
	file = get_object_or_404(SvnPkg, id=fileid)
	#file = SvnPkg.objects.get(id=fileid)
	#get the mirror info
	mirror = Mirror.objects.get(id=mirrorid)
	
	#check the last time this user dl'd the file
	#lets make a var for our session item dltype+id
	sessionVar = "dl_std_%s" % fileid
	if sessionVar in request.session:
		time_now = time.time()
		dltimestamp = request.session[sessionVar]
		if time_now - 2400 >= dltimestamp: #2400=40m (ttl attempt was>=40m ago, inc filecnt,setnewtime)
			incfileday(file)
			incfilemonth(file)
			incbw(file,mirror)
			request.session[sessionVar] = time_now
			dltimestamp = time_now
			pass
		pass
	else:
		dltimestamp = time.time()
		request.session[sessionVar] = dltimestamp
		incfileday(file)
		incfilemonth(file)
		incbw(file,mirror)
		
	return render_to_response('dlst.html', {'file': file,'mirror':mirror,'time':dltimestamp})
	
def seeds(requst,fileid):
	file = SvnPkg.objects.get(id=fileid)
	return render_to_response('dlse.html', {'file': file})
	
def mirrorlist(request):
	mirrors = Mirror.objects.filter(enabled=1)
	return render_to_response('mirrors.html', {'mirrors':mirrors})
