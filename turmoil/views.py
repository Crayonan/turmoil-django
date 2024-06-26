from django.shortcuts import render, redirect
from .models import NavbarItem, Notice, Thumbnail, SiteLogo, Advertisement, Article, Slider
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    context = {
        'navbar_items': NavbarItem.objects.all(),
        'notice': Notice.objects.first(),
        'thumbnails': Thumbnail.objects.all(),
        'site_logo': SiteLogo.objects.first(),
        'advertisements': Advertisement.objects.all(),
        'articles': Article.objects.all(),
        'sliders': Slider.objects.all(),
    }
    return render(request, 'home.html', context)

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'partials/main_container.html', {'form': form})