
from django.urls import path
from courses import views


urlpatterns = [
   
    path('allcourse/',views.home, name = 'home'),
    path('course/<str:slug>',views.coursePage, name = 'coursepage'),
    path('',views.homeActual, name = 'home'),



]

