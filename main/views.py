from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .forms import CreateUser


def read_users(request):
    """Чтение пользователей и запись в файл"""
    rows = User.objects.all()
    for el in rows:
        with open('media/users_read.txt', 'a') as file:
            file.write(f'{el.username};{el.password};{el.date_joined};{el.last_login};{el.is_active};{el.email}\n')
    return render(request, 'main/create_user.html')


def write_users(request):
    """Запись пользователей из файла"""
    with open('media/users_read.txt') as file:
        for line in file:
            user, password, date_joined, last_login, active, email = line.split(';')
            query = QueryDict('password1=Ljcneg2022&password2=Ljcneg2022', mutable=True)
            query.update({
                'username': user,
                'date_joined': date_joined,
                'is_active': active,
            })
            if email:
                query.update({'email': email.rstrip()})
            if last_login is not None:
                query.update({'last_login': last_login})
            form = CreateUser(query)
            print(query)
            if form.is_valid():
                print('valid')
                form.save()
                row = User.objects.filter(username=user).first()
                row.password = password
                row.save()
    return render(request, 'main/create_user.html')
