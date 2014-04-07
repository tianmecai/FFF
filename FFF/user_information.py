from django.http import HttpResponse
from users.models import User
def register(request,_phone,_password):
    if len(User.objects.filter(phone=_phone)) == 0:
        u = User(phone=_phone,password=_password)
        u.save()
        return HttpResponse('0')
    else:
        return HttpResponse('1')
   
def login(request,_phone,_password):
    if len(User.objects.filter(phone=_phone)) == 0:
        return HttpResponse('1')     # not registered
    elif len(User.objects.filter(phone=_phone,password=_password)) == 0:
        return HttpResponse('2')     # wrong password
    else:
        return HttpResponse('0')