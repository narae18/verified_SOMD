import re
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.db.models import Q

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
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
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        gender = request.POST.get('gender')
        birth = request.POST.get('birth')
        year = birth[:4]
        month = birth[4:6]
        day = birth[6:]
        birth = f'{year}-{month}-{day}'
        college = request.POST.get('college')
        department = request.POST.get('department')
        email = request.POST.get('email')

        # 입력값 검증
        if not re.match(r'^[a-zA-Z0-9_-]{4,16}$', request.POST.get('username')):
            messages.error(request, '유효한 아이디 형식이 아닙니다.')
            return redirect('accounts:signup')

        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', request.POST.get('password')):
            messages.error(request, '비밀번호는 영문자, 숫자, 특수문자(@$!%*?&)를 모두 포함하여 8자 이상 입력해야 합니다.')
            return redirect('accounts:signup')

        if request.POST.get('password') != request.POST.get('confirm'):
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('accounts:signup')

        if User.objects.filter(Q(username=request.POST.get('username')) | Q(email=request.POST.get('email'))).exists():
            messages.error(request, '이미 사용 중인 ID 또는 이메일입니다.')
            return redirect('accounts:signup')

        try:
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
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
            )
            profile.save()

            # 회원 가입 완료 후 이메일 인증을 위한 코드 추가
            current_site = get_current_site(request)
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "SOMDI 이메일 인증이 도착했습니다🐘"
            mail_to = request.POST.get("email")
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

            auth.login(request, user)
            messages.success(request, '회원 가입 성공!')
            return redirect('main:mainpage')
        except Exception as e:
            messages.error(request, f'회원 가입 실패: {e}')

    return render(request, 'accounts/signup.html')

def deleteUser(request):
    user = request.user
    user.delete()
    return redirect('main:mainpage')