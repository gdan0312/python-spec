from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def topic_details(request, pk):
    return render(request, 'blog/topic_details.html')
