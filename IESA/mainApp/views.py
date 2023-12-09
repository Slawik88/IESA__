from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def home_page_view(request):
    return render(request, 'mainApp\index.html')


def change_language(request, language):
    # Установить язык сайта
    request.LANGUAGE_CODE = language

    # Перенаправить пользователя на текущую страницу
    return HttpResponseRedirect(request.META['HTTP_REFERER'])