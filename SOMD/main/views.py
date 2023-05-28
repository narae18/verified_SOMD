from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag, SOMD, Member
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
    
def board(request):
    somds = SOMD.objects.all()
    return render(request, 'main/board.html', {"somds": somds})


def register(request):
    return render(request,'main/register.html')

def createSOMD(request):
    if request.user.is_authenticated:
        user = request.user
        new_somd = SOMD()
        new_somd.backgroundimage = request.FILES.get("back_pic")
        new_somd.profileimage = request.FILES.get("profile_pic")
        new_somd.name = request.POST["somdname"]

        if request.POST.get("department"):
            new_somd.department = request.POST["department"]
        elif request.POST.get("college"):
            new_somd.department = request.POST["college"]
        else:
            pass
        
        new_somd.category = request.POST["category"]
        new_somd.intro = request.POST["intro"]
        new_somd.snslink = request.POST["snslink"]
        
        new_somd.save()
        
        member, created = Member.objects.get_or_create(user=user)
        member.somds.add(new_somd)
        
        new_somd.admins.set([user])
        
        return redirect("main:mainfeed", new_somd.id)
    else:
        return redirect('accounts:login')



def mainfeed(request, id):
    user = request.user
    member = Member.objects.get(user=user)
    somds = SOMD.objects.filter(members=member)
    return render(request, "main/mainfeed.html", {
        'somds': somds,
    })
