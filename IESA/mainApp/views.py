from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from mainApp.models import Swiper


def home_page_view(request):
    swiper_images = Swiper.objects.all()
    return render(request, 'mainApp\index.html', {'swiper_images': swiper_images})


def change_language(request, language):
    # Установить язык сайта
    request.LANGUAGE_CODE = language

    # Перенаправить пользователя на текущую страницу
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def slider_views(request):
    sliders = Swiper.objects.all()
    return render(request, 'mainApp\index.html', {'sliders': sliders})
