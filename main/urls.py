from django.urls import path

from . import views
urlpatterns = [
    path('about-us/', views.about_us, name='main/about-us'),
    path('contact-us/',views.contact_us,name='main/contact-us'),
    path('',views.index,name='main/index'),
    path('our-services/',views.our_services,name='main/our-services'),
    path('our-team/',views.our_team_,name='main/our-team'),
    path('pricing/',views.pricing,name='main/pricing'),
    ]
