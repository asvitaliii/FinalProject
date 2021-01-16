from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import MyUser


def index(request):
    return render(request, 'homepage/index.html')


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/personal_account")
        return render(request, 'account/register.html')
    elif request.method == "POST":

        name = request.POST.get('login_field')
        pass1 = request.POST.get('password_field')
        pass2 = request.POST.get('password_confirmation_field')
        data = {'login': name, 'pass1': pass1, 'pass2': pass2}

        if pass1 != pass2:
            messages.error(request, 'Пароли должны совпадать')
            return render(request, 'account/register.html')
        elif '' in data.values():
            messages.error(request, 'Все поля обязательные')
            return render(request, 'account/register.html')
        elif len(pass1) < 8 or len(pass1) > 15:
            messages.error(request, 'Пароль должен быть от 8 до 15 сиволов')
            return render(request, 'account/register.html')
        else:
            user = MyUser.objects.create_user(name, pass1)
            user.save()
            if user:
                messages.success(request, 'Вы успешно зарегестрированы')
                return redirect("/personal_account")
            messages.error(request, 'Неизвестная ошибка')
            return render(request, 'account/register.html')


def ajax_reg(request) -> JsonResponse:
    response = dict()
    name = request.GET.get('login_field')
    try:
        MyUser.objects.get(name=name)
        response['message_login'] = "Логин занят"
    except MyUser.DoesNotExist:
        response['message_login'] = "ОК"
    return JsonResponse(response)


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/personal_account')
        return render(request, 'account/sign_in.html')
    elif request.method == "POST":
        user = authenticate(request, name=request.POST.get('login_field'), password=request.POST.get('password_field'))
        if user is None:
            messages.success(request, 'Пользователь не найден или неверный пароль!')
            return render(request, 'account/sign_in.html')
        else:
            login(request, user)
            return render(request, "homepage/personal_account.html")


def logout_user(request):
    messages.success(request, 'Вы успешно деавторизованы')
    logout(request)
    return redirect("/")


def personal_account(request):
    return render(request, 'homepage/personal_account.html')
