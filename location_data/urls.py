from django.urls import path
from .views import *

urlpatterns=[
    path('location/<str:district_name>/',show_location),
    path('province/<str:province_name>/',show_province_data,name='show_province_data'),
    path('adddistrict/',add_district),
    path('updatedistrict/<int:district_id>/<str:getprovince_name>/',updatedistrict), # i am getting the province name as well so that i can return the district data of that province
    path('deletedistrict/<int:district_id>/<str:getprovince_name>/',deletedistrict),
    path('addlocation/',add_location),
    path('updatelocation/<str:district_name>/<int:location_id>',updatelocation),
    path('deletelocation/<str:district_name>/<int:location_id>',deletelocation),


]