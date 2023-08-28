from django.shortcuts import render, redirect
from django.http import Http404
from .models import ShortenedURL

def index(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = ShortenedURL.generate_unique_short_code()
        ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
        short_url = request.build_absolute_uri(f'/{short_code}')
        return render(request, 'index.html', {'short_url': short_url})
    return render(request, 'index.html')

def redirect_to_original(request, short_code):
    try:
        shortened_url = ShortenedURL.objects.get(short_code=short_code)
        return redirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        raise Http404('Shortened URL not found')
