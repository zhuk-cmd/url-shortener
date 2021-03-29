from django.shortcuts import render, redirect
from .forms import URLForms
from .models import URL
import random, string


def index(request):
    if request.method == 'POST':
        form = URLForms(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            short_url = str(request.build_absolute_uri()) + slug
            data = form.cleaned_data['url']
            new_url = URL(url=data, slug=short_url)
            new_url.save()
    else:
        form = URLForms
    url_data = URL.objects.all()
    context = {
        'form': form,
        'data': url_data
    }
    return render(request, 'index.html', context)


def red(request, slug):
    linc = URL.objects.get(slug=str(request.build_absolute_uri()))
    linc.clicks += 1
    linc.save()
    return redirect(linc.url)