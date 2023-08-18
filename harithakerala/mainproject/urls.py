"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', views.index),
    path('login1/', views.login1),
    path('login3/', views.login3),
    path('sample/', views.sample),
    path('index1/', views.index1),
    
    path('registration/', views.registration),
    path('adminhome/', views.adminhome),

    path('adddistrict_page/', views.adddistrict_page),
    path('adddistrict1/', views.adddistrict1),
    path('removedistrict/', views.removedistrict),
    path('removedistrict1/<str:s1>/', views.removedistrict1),
  
    
    path('addfee/', views.addfee),
    path('addfee1/', views.addfee1),
    path('viewfeeremove/', views.viewfeeremove),
    path('feeremove/<str:s1>/', views.feeremove),
    path('updatefeeview/', views.updatefeeview),
    path('updateviewform/<str:r1>', views.updateviewform),
    path('updatefee/<str:r1>', views.updatefee),
    path('viewcomplaint/', views.viewcomplaint),


    path('dishome/', views.dishome),
    path('addlocalbody/', views.addlocalbody),
    path('addlocalbody1/', views.addlocalbody1),
    path('removelocalbody/', views.removelocalbody),
    path('removelocalbody1/<str:s1>/', views.removelocalbody1),



    path('localhome/', views.localhome),
    path('addward/', views.addward),
    path('addward1/', views.addward1),
    path('removeward/', views.removeward),
    path('removeward1/<str:s1>/', views.removeward1),


    path('harithakarmasenaemp/', views.harithakarmasenaemp),
    path('house1/', views.house1),
    path('addhouse/', views.addhouse),
    path('removehouse/', views.removehouse),
    path('removehouse1/<str:s1>/', views.removehouse1),

    path('dutyview/', views.dutyview),
    path('duty1/', views.duty1),
    path('removeduty/', views.removeduty),
    path('removeduty1/<str:s1>/', views.removeduty1),
    path('updatedutyview/', views.updatedutyview),
    path('updatedutyform/<str:r1>', views.updatedutyform),
    path('updateduty/<str:r1>', views.updateduty),

    path('hksemp/', views.hksemp),
    path('hksemp1/', views.hksemp1),
     path('removehks/', views.removehks),
    path('removehks1/<str:s1>/', views.removehks1),


    path('wardhouse/', views.wardhouse),
    

    path('househome/', views.househome),
    path('housecomplaint/', views.housecomplaint),
    path('housecomplaint1/', views.housecomplaint1),

    path('public/', views.public),
    path('application/', views.application),
    path('application1/', views.application1),
    path('viewapplication/', views.viewapplication),
    path('acceptharithakarma/<str:id>',views.acceptharithakarma),
    # path('rejectharithakarma/<str:id>',views.rejecthraithakarma),
    

    path('allotward/', views.allotward),
    path('allotward1/<str:id>', views.allotward1),
    path('allotward2/', views.allotward2),

    path('allothouse/', views.allothouse),
    path('allothouse1/<str:id>', views.allothouse1),
    path('allothouse2/', views.allothouse2),

    path('viewhks/', views.viewhks),

    path('viewwardhks/', views.viewwardhks),
    path('viewhousehks/', views.viewhousehks),
    path('housecollection/<str:id>', views.housecollection),
    path('housecollection1/', views.housecollection1),

    path('hkscomplaint/', views.hkscomplaint),
    path('hkscomplaint1/', views.hkscomplaint1),

    path('hksemployeehome/', views.hksemployeehome),

 

    path('housecollectionview/', views.housecollectionview),

    path('houseowner/', views.houseowner),
    path('functiondetails/', views.functiondetails),
    path('functiondetails1/', views.functiondetails1),

    path('viewfunctiondetails/', views.viewfunctiondetails),
    path('foodbalances/<str:id>', views.foodbalances),
    path('foodbalances1/', views.foodbalances1), 
    
    path('viewfunctionhks/', views.viewfunctionhks),
    path('acceptfunction/<str:id>',views.acceptfunction),
    path('rejectfunction/<str:id>',views.rejectfunction),
     
    path('viewfoodbalance/', views.viewfoodbalance),
    path('foodcollectionpoint/<str:r1>', views.foodcollectionpoint),
    path('foodcollectionpoint1/<str:r1>', views.foodcollectionpoint1),


   

    path('viewfoodbalancerequest/', views.viewfoodbalancerequest),  
    path('foodrequest/<str:id>', views.foodrequest), 
    path('foodrequest1/', views.foodrequest1),
    path('viewfoodrequest/', views.viewfoodrequest),
    path('acceptfoodrequest/<str:id>',views.acceptfoodrequest),
    path('rejectfoodrequest/<str:id>',views.rejectfoodrequest), 

    path('viewrequestlocalbody/', views.viewrequestlocalbody),
    path('viewrequestward/<str:id>', views.viewrequestward),
    path('viewrequesthouse/<str:id>', views.viewrequesthouse),

    path('viewhousepayment/', views.viewhousepayment),
    path('payments/<str:id>', views.payments),
    path('payment1/', views.payment1),

    path('viewfunctiondetailscollections/', views.viewfunctiondetailscollections),
    path('viewcollectionpointhouse/<str:id>', views.viewcollectionpointhouse),
    path('adminreport/', views.adminreport),

    path('adminlogout/', views.adminlogout),
    path('districtlogout/', views.districtlogout),
    path('localbodylogout/', views.localbodylogout),
    path('hkslogout/', views.hkslogout),
    


    # path('adminlogout/', views.adminlogout),







]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)