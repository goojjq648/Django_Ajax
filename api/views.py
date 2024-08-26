from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Member
import time
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password

# Create your views here.
def checkNameValid(name):
    if not name:
        return False, '請輸入姓名'

    if len(name) > 20:
        return False, '姓名不能超過20個字'

    members = Member.objects.filter(user_name=name)
    if members.exists():
        return False, '姓名已被註冊過'

    return True, ''


def checkPasswordValid(password, passwordConfirm):
    if not password:
        return False, '請輸入密碼'
    if not passwordConfirm:
        return False, '請輸入密碼確認'
    if password != passwordConfirm:
        return False, '密碼輸入的不一致，請再確認一次'

    return True, ''

def checkEmailValid(email):
    if not email:
        return False, '請輸入電子信箱'
    
    members = Member.objects.filter(user_email=email)
    if members.exists():
        return False, '電子信箱已被註冊過'

    return True, '電子信箱可以註冊'

def register(request):
    name = request.POST.get('name', 'Guest')
    email = request.POST.get('email', 'Guest@company.com')
    age = request.POST.get('age', 18)

    password = request.POST.get('password')
    passwordConfirm = request.POST.get('passwordConfirm')

    # 姓名驗證
    isvalid, msg = checkNameValid(name)
    if not isvalid:
        return returnRegisterInfo(isvalid, '', msg)
    
    # 電子信箱驗證
    isvalid, msg = checkEmailValid(email)
    if not isvalid:
        return returnRegisterInfo(isvalid, '', msg)

    # 密碼驗證
    isvalid, msg = checkPasswordValid(password, passwordConfirm)
    if not isvalid:
        return returnRegisterInfo(isvalid, '', msg)

    # 檔案上傳
    uploaded_file = request.FILES.get('avator')
    file_name = ''
    if uploaded_file:
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)

    content = f'''您好，
    您的註冊資訊如下：
    姓名：{name} /n
    電子信箱: {email} /n
    年紀：{age} /n
    上傳:{file_name}'''

    Member.objects.create(
        user_name=name,
        user_password=make_password(password),
        user_email=email,
        user_age=age,
        user_avator=file_name
    )

    return returnRegisterInfo(True, content, '')


def fetchCheckEmailValid(request):
    email = request.GET.get('email')

    isValid, msg = checkEmailValid(email)

    return returnRegisterInfo(isValid, '電子信箱可以註冊', msg) 

def fetchCheckAccValid(request):
    name = request.GET.get('name')

    isValid, msg = checkNameValid(name)

    return returnRegisterInfo(isValid, '帳號可以註冊', msg)


def returnRegisterInfo(isValid, successfulMsg, errorMsg):
    msg = ''

    if isValid:
        msg = successfulMsg
    else:
        msg = errorMsg

    response_data = {
        'success': isValid,
        'message': msg
    }

    return JsonResponse(response_data)
