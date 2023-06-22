from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag, SOMD, Member, Images, JoinRequest
from django.contrib.auth.models import User
from django.utils import timezone
import re
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.


def mainpage(request):
    if request.user.is_authenticated:
        user = request.user
        members = Member.objects.filter(user=user)
        somds = SOMD.objects.filter(members__in=members)
        if somds:
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
        if "back_pic" in request.FILES:
            new_somd.backgroundimage = request.FILES["back_pic"]
        else:
            default_image_path = "somd/somdbackDefaultImage.png"
            default_image_content = default_storage.open(default_image_path).read()
            default_image_file = ContentFile(default_image_content)
            new_somd.backgroundimage.save("somdbackDefaultImage.png", default_image_file)
        
        if "profile_pic" in request.FILES:
            new_somd.profileimage = request.FILES["profile_pic"]
        else:
            default_profile_image_path = "somd/somdDefaultImage.png"
            default_profile_image_content = default_storage.open(default_profile_image_path).read()
            default_profile_image_file = ContentFile(default_profile_image_content)
            new_somd.profileimage.save("somdDefaultImage.png", default_profile_image_file)
    
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

        tag_text = request.POST.get("tag")  # 선택된 태그 텍스트
        tag, created = Tag.objects.get_or_create(name=tag_text)
        new_somd.tags.set([tag])

        member, created = Member.objects.get_or_create(user=user)
        member.somds.add(new_somd)
        new_somd.admins.set([user])

        return redirect("main:mainfeed", new_somd.id)
    else:
        return redirect('accounts:login')



def mainfeed(request, id):
    # user = request.user
    # member = Member.objects.get(user=user)
    somd = SOMD.objects.get(id=id)
    posts = somd.somds.all()
    return render(request, "main/mainfeed.html", {
        'somd': somd,
        'posts':posts
    })

def mysomd(request):
    user = request.user
    try:
        member = Member.objects.get(user=user)
    except Member.DoesNotExist:
        return render(request, "main/mysomd.html")
        
    member = Member.objects.get(user=user)
    somds = member.somds.all()
    tags = Tag.objects.all()
    return render(request, "main/mysomd.html", {
        'somds': somds,
        'tags':tags,
    })
    
def new(request,somd_id):
    somd = SOMD.objects.get(id=somd_id)
    return render(request, 'main/new.html', {'somd': somd})

def createpost(request, somd_id):
    # if request.user in SOMD.members:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            writer = request.user
            somd = SOMD.objects.get(id=somd_id)

            new_post = Post.objects.create(
                title=title,
                writer=writer,
                pub_date=timezone.now(),
                content=content,
                somd=somd
            )

            images = request.FILES.getlist('images')
            for image in images:
                new_image = Images.objects.create(post=new_post, image=image)

            return render(request, 'main/viewpost.html', {'post': new_post, 'images': new_post.images.all()})
        
def viewpost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        images = post.images.all()
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/viewpost.html', {
            'post': post,
            'images': images,
            'comments': comments
            })
    # elif request.method == 'POST':
    #     if request.user.is_authenticated:
    #         new_comment = Comment()
    #         new_comment.post = post
    #         new_comment.writer = request.user
    #         new_comment.content = request.GET["comment"]
    #         new_comment.pub_date = timezone.now()
    #         new_comment.save()

    #         return redirect('main/viewpost.html', post.id)
            
