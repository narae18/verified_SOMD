from django.shortcuts import render
from main.models import Member

# Create your views here.
def mypage(request):
    user = request.user
    try:
        member = Member.objects.get(user=user)
    except Member.DoesNotExist:
        return render(request, "users/mypage.html")
        

    member = Member.objects.get(user=user)
    somds = member.somds.all()
    return render(request, "users/mypage.html", {
        'somds': somds,
    })