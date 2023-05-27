from django.shortcuts import render, redirect

# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')

def test(request):
    return render(request, 'main/test.html')

def register(request):
    return render(request,'main/register.html')

def createSOMD(request):
    if request.user.is_authenticated:
        return redirect("main:mainpage")
    else:
        return redirect('accounts:login')