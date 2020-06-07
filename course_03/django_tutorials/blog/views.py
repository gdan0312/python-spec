from django.db.models import Count
from django.http import Http404
from django.shortcuts import render

from blog.models import Topic, Category


def index(request):
    topics = Topic.objects.all().annotate(Count('categories'))
    categories = Category.objects.all()
    q = request.GET.get('q')
    category_pk = request.GET.get('category')

    if q is not None:
        topics = topics.filter(title__icontains=q)

    if category_pk is not None:
        topics = topics.filter(categories__pk=category_pk)

    return render(request, 'blog/index.html', context={
        'topics': topics,
        'categories': categories
    })


def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'blog/topic_details.html', context={
        'topic': topic
    })
