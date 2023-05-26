from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')

def test(request):
    return render(request, 'main/test.html')