import json
import requests
import logging
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.views.generic import UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from News.models import Category, ArtiLes, Comment
from News.serializers import ArtiLesSerializer, CategorySerializer, CommentSerializer
from django.http import JsonResponse
from django.db.models import Q
from django.views import View
from django.urls import reverse
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

def search(request):
    query = request.GET.get('q', '')

    if query:
        products = ArtiLes.objects.filter(
            Q(title__icontains=query) | Q(full_text__icontains=query)
        )
        products_list = [
            {
                'title': product.title,
                'full_text': product.full_text,
                'url': reverse('product_detail', args=[product.id])
            }
            for product in products
        ]
    else:
        products_list = []

    response_data = {
        'query': query,
        'products': products_list,
    }

    return JsonResponse(response_data)


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(ArtiLes, pk=pk)

        product_data = {
            'title': product.title,
            'full_text': product.full_text,
            'id': product.id
        }

        return JsonResponse(product_data)


def weather(request):
    weather_api_key = 'e1b9079f105bdb7e3abaabfe82dcf8a8'
    city = request.GET.get('city', 'Almaty')
    weather_data = {}
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'

    try:
        response_weather = requests.get(weather_url)
        response_weather.raise_for_status()
        weather_data = response_weather.json()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Error fetching weather data'}, status=500)
    return JsonResponse({'weather': weather_data})
    return JsonResponse(context)


def currency(request):
    base_currency = request.GET.get('base', 'KZT')
    currencies_to_display = request.GET.getlist('currencies')
    currency_url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    try:
        response_currency = requests.get(currency_url)
        response_currency.raise_for_status()
        currency_data = response_currency.json()
        logger.info(f"Ответ от API валют: {currency_data}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка API валют: {e}")
        currency_data = None

    if currency_data:
        all_rates = currency_data.get('rates', {})
        filtered_rates = {currency: all_rates[currency] for currency in currencies_to_display if currency in all_rates}

        context = {
            'base_currency': base_currency,
            'rates': filtered_rates
        }
    else:
        context = {
            'error': 'Не удалось получить данные о валюте.'
        }

    return JsonResponse(context)


#-------------------------api---------------
class CategotyApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArtiLesApi(viewsets.ModelViewSet):
    queryset = ArtiLes.objects.all()
    serializer_class = ArtiLesSerializer
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

class CommentApi(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer