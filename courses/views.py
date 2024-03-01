from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course,Video


def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,'courses/home.html',context = {"courses":courses})

def homeActual(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,'courses/homeActual.html',context = {"courses":courses})

def coursePage(request,slug):
    print(request.user.is_authenticated)
    # print(slug)
    course = Course.objects.get(slug = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number= 1
    video = Video.objects.get(serial_number = serial_number,course=course)

    if((request.user.is_authenticated is False) and (video.is_preview is False)):
        return HttpResponse("Please login")
    
        


    print(video)
    # print(serial_number,course)

    context = {"course":course,
               "video":video,
               "videos": videos
               
               }
    return render(request,template_name='courses/course_page.html',context = context)    