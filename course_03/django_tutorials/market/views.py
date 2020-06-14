import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from .models import Item, Review
from.schemas import ADD_ITEM_SCHEMA, POST_REVIEW_SCHEMA


class AddItemView(View):
    """
    View для создания товара
    """
    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, ADD_ITEM_SCHEMA)
            item = Item.objects.create(title=document['title'],
                                       description=document['description'], price=document['price'])
            return JsonResponse({'id': item.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': e.message}, status=400)


class PostReviewView(View):
    """
    View для создания отзыва о товаре
    """
    def post(self, request, item_id):
        try:
            document = json.loads(request.body)
            validate(document, POST_REVIEW_SCHEMA)
            item = Item.objects.get(id=item_id)
            review = Review.objects.create(text=document['text'], grade=document['grade'], item=item)
            return JsonResponse({'id': review.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': e.message}, status=400)
        except Item.DoesNotExist:
            return HttpResponse(status=404)


class GetItemView(View):
    """
    View для получения информации о товаре
    Помимо основной информации выдает последние отзывы о товаре не более 5 штук
    """
    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            reviews = Review.objects.filter(item__id=item_id)
            reviews_count = reviews.count()
            reviews_ = []
            if 1 <= reviews_count <= 5:
                reviews_ = [{'id': review.id, 'text': review.text, 'grade': review.grade} for review in reviews]
            elif reviews_count > 5:
                for review in reviews.order_by('-id')[:5]:
                    reviews_.append({'id': review.id, 'text': review.text, 'grade': review.grade})
            return JsonResponse({
                'id': item.id,
                'title': item.title,
                'description': item.description,
                'price': item.price,
                'reviews': reviews_
            })
        except Item.DoesNotExist:
            return HttpResponse(status=404)
