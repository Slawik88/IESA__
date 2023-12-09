from django.contrib import admin

from .models import Swiper


@admin.register(Swiper)
class SwiperAdmin(admin.ModelAdmin):
    list_display = ('image',)

    def save_model(self, request, obj, form, change):
        if request.FILES['image']:
            obj.image = request.FILES['image']
        obj.save()
