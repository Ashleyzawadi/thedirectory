from django.shortcuts import get_object_or_404, render
from .models import Agency, Agent
from django.http import HttpResponse,Http404
# from django.core.exceptions import DoesNotExist
# Create your views here.
def home(request):
    all_agencies = Agency.objects.all()
    context = {'all_agencies':all_agencies}  
    return render(request, 'index.html', context)

def agency_detail(request, agency_id):

    try:
        agency = Agency.objects.get(pk = agency_id)
    except Agency.DoesNotExist:
        raise Http404()
        # context = {'agency':agency}
    return render(request, 'agencies/agency.html',{'agency':agency,})

