from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
<<<<<<< HEAD

from mainApp.models import Swiper


def home_page_view(request):
    swiper_images = Swiper.objects.all()
    return render(request, 'mainApp\index.html', {'swiper_images': swiper_images})
=======


def home_page_view(request):
    return render(request, 'mainApp\index.html')
>>>>>>> 51bee0cf41382f408dd2e93e054c6c3acdb3edb9


def change_language(request, language):
    # Установить язык сайта
    request.LANGUAGE_CODE = language

    # Перенаправить пользователя на текущую страницу
<<<<<<< HEAD
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def slider_views(request):
    sliders = Slider.objects.all()
    return render(request, 'mainApp\index.html', {'sliders': sliders})
=======
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
>>>>>>> 51bee0cf41382f408dd2e93e054c6c3acdb3edb9
