from django.urls import path
from .views import *


urlpatterns=[
    path('',homepage),
    path('registeruser/',register_user),
    path('login/',login_user),
    path('logout',log_out)

]