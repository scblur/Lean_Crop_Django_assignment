from django.shortcuts import render
from .models import FarmerData, FarmData, ScheduleData
from django.shortcuts import get_object_or_404, redirect
import datetime
# Create your views here.

def farmer_list(request):
    farmers = FarmerData.objects.all().order_by('-created_date')
    return render(request, "farmer_list.html", {"farmers":farmers})

def farm_list(request):
    farms = FarmData.objects.all().order_by('-created_date')
    return render(request, "farm_list.html", {"farms":farms})

def schedule_list(request):
    schedule = ScheduleData.objects.all().order_by('-created_date')
    farms = FarmData.objects.all().order_by('-created_date')
    return render(request, "schedule_list.html", {"schedule":schedule,"farms":farms})
