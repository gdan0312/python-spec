import json

from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from marshmallow.exceptions import ValidationError as MarshmallowError

from .models import Feedback
from .schemas import REVIEW_SCHEMA, ReviewSchema


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FeedbackListView(LoginRequiredMixin, ListView):
    model = Feedback

    def get_queryset(self):
        if self.request.user.is_stuff:
            return Feedback.objects.all()
        return Feedback.objects.filter(author=self.request.user)


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
