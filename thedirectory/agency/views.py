from django.shortcuts import render
from .models import Agency, Agent
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    all_agencies = Agency.objects.all()
    context = {'all_agencies':all_agencies}  
    return render(request, 'index.html', context)

def agency_detail(request, pk):
    
    agency = get_object_or_404(Agency,pk=pk)
    
    context = {'agency':agency},  
    return (request, 'agency.html', context)
