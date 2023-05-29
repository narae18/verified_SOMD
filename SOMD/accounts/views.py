from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        else:
            return render(request,'accounts/login.html')
        
    elif request.method == "GET":
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect("main:mainpage")


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        nickname = request.POST['nickname']
        gender = request.POST['gender']
        year = request.POST['year']
        month = request.POST['month']
        day = request.POST['day']
        college = request.POST['college']
        department = request.POST['department']

        username = request.POST['username']
        password = request.POST['password']
        email_id = request.POST['email_id']
        email_addr = request.POST['email_addr']


        # # 정규식 및 유효성 검사
        # if not re.match('^[a-zA-Z0-9_-]{5,20}$', username):
        #     messages.error(request, '올바른 ID 형식이 아닙니다.')
        #     return redirect('/')
        
        # if not re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$', password):
        #     messages.error(request, '올바른 비밀번호 형식이 아닙니다.')
        #     return redirect('/')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 사용 중인 ID입니다.')
            return redirect('/')
        
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']

            )
        user.email = email_id + '@' + email_addr
        user.save()
        # 추가 필드 정보 저장
        birthday = year + '-' + month + '-' + day
        profile = Profile(
            user=user,
            name=name,
            nickname=nickname,
            gender=gender,
            birthday=birthday,
            college=college,
            department=department
        )
        profile.save()
        auth.login(request,user)

        return redirect('main:mainpage')

    return render(request, 'accounts/signup.html')
    