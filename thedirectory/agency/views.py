from django.shortcuts import get_object_or_404, render
from .models import Agency, Agent
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    all_agencies = Agency.objects.all()
    # context = {'all_agencies':all_agencies}  
    return render(request, 'index.html', locals())

def agency_detail(request, agency_id):

    try:
        agency = Agency.objects.get(pk = agency_id)
    except Agency.DoesNotExist:
        raise Http404()
        # context = {'agency':agency}
    return render(request, 'agencies/agency.html',{'agency':agency,})

