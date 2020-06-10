import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from marshmallow.exceptions import ValidationError as MarshmallowError

from .forms import DummyForm
from .schemas import REVIEW_SCHEMA, ReviewSchema


class FormDummyView(View):
    def get(self, request):
        form = DummyForm()
        return render(request, 'form.html', context={'form': form})

    def post(self, request):
        form = DummyForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context=context)
        return render(request, 'error.html', context={'errors': form.errors})


class SchemaView(View):
    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as err:
            return JsonResponse({'errors': err.message}, status=400)


class MarshView(View):
    def post(self, request):
        try:
            document = json.loads(request.body)
            schema = ReviewSchema(strict=True)
            data = schema.load(document)
            return JsonResponse(data.data, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except MarshmallowError as err:
            return JsonResponse({'errors': err.messages}, status=400)
