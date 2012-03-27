# Create your views here.
from glua.svn.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
import pysvn,os
def index(request):
	activedls = SvnPkg.objects.filter(pkg_active=1).order_by('pkg_shortname')
	pgtitle = "index"
	pgjs = "index"
	cats = SvnPkgCat.objects.all()
	for dl in activedls:
		dl.repolist = dl.pkg_repos.all()
	return render_to_response('dls.html', {'activedls': activedls,'cats':cats,'title':pgtitle,'pgjs':pgjs,})

def updater(): #updates the svns,runs the svnsync, and packages
	#set things up
	updated = list()						#create the list of updated svns
	client = pysvn.Client()					#create the svn client?
	#iterate
	activesvns = SvnRepo.objects.filter(svn_active=1)		#get all our active svns.
	for activesvn in activesvns:					#for each svn in our active svns
		#activesvn.svn_shortname					#the shortname for the svn
		#lets setup the username/pass var
		if activesvn.svn_uname:
			#client.callback_get_login = lambda realm,username,may_save:(True, activesvn.svn_uname, activesvn.svn_pass, False) #I'm not sure how this works :d
			#define some globals
			global svn_uname,svn_pass,retcode
			svn_uname =  activesvn.svn_uname
			svn_pass = activesvn.svn_pass
			retcode = True
			client.callback_get_login = svn_login
		else:
			client.callback_get_login = None
		if os.path.exists("checkout/%s" % activesvn.svn_cofolder):	#check that the checkout folder exists
			print "Checking Whether the SVN (%s) has Changed or not." % activesvn.svn_shortname
			remoterev = int(os.popen("svn info %s | grep Revision:" % activesvn.svn_url, 'r').read().rpartition(': ')[2].strip("\n"))#man this is ugly
			localrev = int(client.info("checkout/%s" % activesvn.svn_cofolder).revision.number)						#notasugly :D
			print "Local: %s | Remote: %s" % (remoterev, localrev)
			if remoterev != localrev:			#oh look, we might update
				print "Revisions Not Equal. Boo!"
				client.update("checkout/%s" % activesvn.svn_cofolder)#checkout
				svnsync(activesvn.svn_cofolder)			#svnsync
				updated.append(activesvn.id)
				currentrev = int(client.info("checkout/%s" % activesvn.svn_cofolder).revision.number) #write the rev# to the db
				activesvn.svn_presentrev = currentrev
				print "Checked out Rev#%s" %currentrev
				activesvn.save()
				pass
			else:						#or not
				print "Revisions are Equal Hooray!"			#do nothing
				pass
		else:							#whoops no folder
			print "Folder for %s Doesn't Exist, Making & Checking Out" % activesvn.svn_shortname
			os.mkdir("checkout/%s" % activesvn.svn_cofolder)	#let's make one.
			#and then checkout
			client.checkout(activesvn.svn_url, "checkout/%s" %activesvn.svn_cofolder)#checkout
			svnsync(activesvn.svn_cofolder)						#sync
			updated.append(activesvn.id)
			currentrev = int(client.info("checkout/%s" % activesvn.svn_cofolder).revision.number) #write the rev# to the db
			activesvn.svn_presentrev = currentrev
			print "Checked out Rev#%s" %currentrev
			activesvn.save()
	print updated
	#lets do a query! (we grab all the packages that are updateable AND active
	result = SvnPkg.objects.filter(pkg_repos__in=updated).filter(pkg_active=True).distinct()
	#print result
	for pkg in result:
		svnpkg(pkg)
  
def svnsync(svn_cof): 						#Does The Export | takes one arg, the svn_cofolder
	print "Syncing Revision to the Build Folder"
	os.system("rsync -aC \"checkout/%s\" build/" % svn_cof)
def svnpkg(svn_pkg):
	repos = svn_pkg.pkg_repos.all()
	print "Packaging SVN %s" % svn_pkg.pkg_shortname
	print "Building ZIP"
	os.system("rm packages/%s.zip" % svn_pkg.pkg_filename)
	folderlist = []
	for repo in repos:
		folderlist.append(repo.svn_cofolder.replace(" ","\ "))
	folderlist = " ".join(folderlist)
	os.system("cd build/ && zip -rq ../packages/%s.zip %s" % (svn_pkg.pkg_filename, folderlist))
	size = float(os.path.getsize("packages/%s.zip" % svn_pkg.pkg_filename))/1000000
	svn_pkg.pkg_size=size
	svn_pkg.save()
	print "Done Building Zip"
def svn_login(realm, username, may_save):
	return retcode, svn_uname, svn_pass, False



#shell cmds
#from glua.svn.models import *
#from glua.svn.views import updater
#import pysvn,os
#