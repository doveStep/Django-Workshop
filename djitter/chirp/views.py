from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from chirp.models import *

def back_to_home(req):
	# Maps accounts/profile back to home (we don't use it)
	return redirect('home')
