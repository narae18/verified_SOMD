import re
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.db.models import Q
from django.dispatch import receiver
from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:mainPage')
        else:
            login_success = False
            return render(request, 'accounts/login.html', {'login_success': login_success})
        
    elif request.method == "GET":
        login_success = True
        return render(request, 'accounts/login.html', {'login_success': login_success})

# def login(request):
#         if request.method == "POST" :
#             username = 'guest';
#             password = 'simbaton'

def logout(request):
    auth.logout(request)
    return redirect("main:start") 

def needTologin(request):
    return render(request,'accounts/needTologin.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        nickname = request.POST['nickname']
        gender = request.POST['gender']
        birth = request.POST['birth']
        year = birth[:4]
        month = birth[4:6]
        day = birth[6:]
        birth = f'{year}-{month}-{day}'
        college = request.POST['college']
        department = request.POST.get('department')
        email = request.POST['email']
        dgu_pass = request.POST.get('dgu_pass', '')
        dgu_pass_approved = False

 
        if not re.match(r'^[a-zA-Z0-9_-]{4,16}$', request.POST['username']):
            # messages.error(request, '유효한 아이디 형식이 아닙니다.')
            return redirect('accounts:signup')

        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', request.POST['password']):
            # messages.error(request, '비밀번호는 영문자, 숫자, 특수문자(@$!%*?&)를 모두 포함하여 8자 이상 입력해야 합니다.')
            return redirect('accounts:signup')

        if request.POST['password'] != request.POST['confirm']:
            # messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('accounts:signup')

        if User.objects.filter(Q(username=request.POST['username']) | Q(email=request.POST['email'])).exists():
            # messages.error(request, '이미 사용 중인 ID 또는 이메일입니다.')
            return redirect('accounts:signup')

        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()

            # 추가 필드 정보 저장
            profile = Profile(
                user=user,
                name=name,
                nickname=nickname,
                gender=gender,
                birthday=birth,
                college=college,
                department=department,
                email=email,
                dgu_pass=dgu_pass,
                dgu_pass_approved=False,
            )
            # profile.save()

            messages.warning(request, '동국 패스 인증 중! 승인 시 로그인 페이지로 이동합니다.')
            return dgupass_process(request, user.id)

<<<<<<< HEAD
=======
            auth.login(request, user)
            messages.success(request, '회원 가입이 완료되었습니다.')
            return redirect('main:mainPage')
>>>>>>> b06ea09bf0ebe12b0c522bfe529ba63fc62847e1
        except Exception as e:
            messages.error(request, '회원 가입 중 오류가 발생했습니다. 다시 시도해주세요.')

    return render(request, 'accounts/signup.html')




def dgupass_process(request,user_id):
    profile = Profile.objects.get(user=user_id)
    if profile.dgupass_approved :
        return redirect('accounts:firstlogin')
    pass

def deleteUser(request):
    user = request.user
    user.delete()
    return redirect('main:mainPage')