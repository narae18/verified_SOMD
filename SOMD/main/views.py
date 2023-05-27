from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag, SOMD
from django.contrib.auth.models import User
from django.utils import timezone
import re
# Create your views here.
def mainpage(request):
    if request.user.is_authenticated:
        user = request.user
        somds = SOMD.objects.filter(members__user=user)
        if somds.exists():
            return render(request, 'main/mainpage.html', {'somds': somds})
    return render(request, 'main/mainpage.html')
    
def test(request):
    return render(request, 'main/test.html')

def register(request):
    return render(request,'main/register.html')

def createSOMD(request):
    if request.user.is_authenticated:
        new_somd = SOMD()
        new_somd.backgroundimage = request.FILES.get("back_pic")
        new_somd.profileimage = request.FILES.get("profile_pic")
        new_somd.name = request.POST["somdname"]

        if request.POST["department"] is not None:
            new_somd.department = request.POST["department"]
        elif request.POST["college"] is not None:
            new_somd.department = request.POST["college"]
        else:
            pass
        
        new_somd.category = request.POST["category"]
        new_somd.intro = request.POST["intro"]
        new_somd.snslink = request.POST["snslink"]
        new_somd.admins = request.user
        new_somd.save()
        return redirect("main:mainpage", new_somd.id)
    else:
        return redirect('accounts:login')