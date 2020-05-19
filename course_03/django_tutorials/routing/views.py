from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def simple_route(request):
    return HttpResponse()


def slug_route(request, slug):
    return HttpResponse(slug)


def sum_route(request, a, b):
    a = int(a)
    b = int(b)
    return HttpResponse(a + b)


@require_GET
def sum_get_method(request):
    params = request.GET
    try:
        a = int(params.get('a'))
        b = int(params.get('b'))
    except (TypeError, ValueError):
        return HttpResponse(status=400)
    return HttpResponse(a + b)


@require_POST
def sum_post_method(request):
    params = request.POST
    try:
        a = int(params.get('a'))
        b = int(params.get('b'))
    except (TypeError, ValueError):
        return HttpResponse(status=400)
    return HttpResponse(a + b)
