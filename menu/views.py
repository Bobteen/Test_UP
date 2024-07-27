from django.shortcuts import render


def home(request):
    return render(request, 'menu/home.html')


def about(request):
    return render(request, 'menu/about.html')


def team(request):
    return render(request, 'menu/team.html')


def services(request):
    return render(request, 'menu/services.html')


def development(request):
    return render(request, 'menu/development.html')


def design(request):
    return render(request, 'menu/design.html')
