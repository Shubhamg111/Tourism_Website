from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from . forms import *

# Create your views here.

def show_location(request,district_name):
    district = District.objects.get(district_name=district_name)
    getlocationdata=Location.objects.filter(district=district)
    context={
        'location_inf':getlocationdata
    }
    return render(request, 'location_data/location.html',context)


def show_province_data(request,province_name):
    province_inf=District.objects.filter(province=province_name)
    context={
        'province_inf':province_inf
    }
    return render(request,'location_data/province.html',context)

# this is to add district. After we add the district it should redirect to showing all data about the district with respective to their province. so to achieve this some modification has been done.
# we do not want to see data of all the province if we are inserting data of district in bagmati province only
def add_district(request):
    if request.method=='POST':
        form=DistrictForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'District added succesfully')
            return redirect('/adddistrict')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add district')
            return render(request,'location_data/add_district.html',{'forms':form})
    
    context={
        'forms':DistrictForm
    }
    return render(request, 'location_data/add_district.html',context)


# deleting the district. Here the same problem as adding district occurs since we only want to show data of a single province, we need the province name as well to send it to show_provibe_data function from urls.py
# looks so simple but is so complicated.
def deletedistrict(request,district_id,getprovince_name):
    getdistrict=District.objects.get(id=district_id)
    getdistrict.delete()
    messages.add_message(request,messages.SUCCESS,'District deleted successfully')
    return redirect('show_province_data',province_name=getprovince_name)

# updating the district
def updatedistrict(request,district_id,getprovince_name):
    instance=District.objects.get(id=district_id)
    if request.method=='POST':
        form=DistrictForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'District is updated')
            return redirect('show_province_data',province_name=getprovince_name)
        else:
            messages.add_message(request, messages.ERROR, 'failed to update District')
            return render(request, 'location_data/update_district.html',{'forms':form})

    context={
        'forms':DistrictForm(instance=instance)
    }
    return render(request,'location_data/update_district.html',context)
    


# this is to add location
def add_location(request):
    if request.method=='POST':
        form=LocationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'location added successfully')
            return redirect('/location')
        else:
            messages.add_message(request,messages.ERROR,'failed to add location')
            return render(request,'location_data/add_location.html',{'forms':form})
    
    context={
        'locationforms':LocationForm
    }
        
    return render(request,'location_data/add_location.html',context)

    # this is to update location, similar to update district
def updatelocation(request,district_name,location_id):
    locationInstance=Location.objects.get(id=location_id)
    if request.method=='POST':
        form=LocationForm(request.POST,request.FILES,instance=locationInstance)
        if form.is_valid:
            form.save()
            messages.add_message(request,messages.SUCCESS,'Location Updated successfully')
            return redirect('/location')
        else:
            messages.add_message(request,messages.ERROR,'Failed to update Location')
            return render(request,'location_data/update_location.html',{'forms':form})

    context={
        'forms':LocationForm(instance=locationInstance)
    }
    return render(request,'location_data/update_location.html',context)


def deletelocation(request,district_name,location_id):
    getlocation=Location.objects.get(id=location_id)
    getlocation.delete()
    messages.add_message(request,messages.SUCCESS,'Location deleted successfully')
    return redirect('/location')