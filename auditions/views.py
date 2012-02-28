# Create your views here.
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from auditions.forms import *

def signup(request):

    if request.method == 'POST':
        # the form is currently static it will need to have dynamic elements at some point
        form = AuditionForm(request.POST)
        #formb = AuditionForm2(request.POST)
        #formc = AuditionForm3(request.POST)
        if form.is_valid(): #and formb.is_valid() and formc.is_valid():
            form.save()
            #formb.save()
            #formc.save()
            return redirect('/audition/success/')

    else:
        form = AuditionForm()
        #formb = AuditionForm2()
        #formc = AuditionForm3()

    return render_to_response('form.html', {'form':form}, context_instance=RequestContext(request))
