from modeltranslation.translator import register

from modeltranslation.translator import TranslationOptions
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Event, Participant


# Регистрация модели Event для перевода
@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('name', 'organizer', 'responsible_person', 'location', 'category', 'description', 'items_to_bring')


# Регистрация модели Event в административной панели
@admin.register(Event)
class EventAdmin(TranslationAdmin, SortableAdminMixin):
    class Media:
        js = [
            'https://code.jquery.com/jquery-3.6.4.min.js',
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',  # Используйте версию jQuery UI из того же источника
            'modeltranslation/js/tabbed_translation_fields.js',
        ]
        css = {
            'screen': ['modeltranslation/css/tabbed_translation_fields.css'],
        }



# Регистрация модели Participant для перевода
@register(Participant)
class ParticipantTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


# Регистрация модели Event в административной панели
@admin.register(Participant)
class ParticipantAdmin(TranslationAdmin, SortableAdminMixin):
    class Media:
        js = [
            'https://code.jquery.com/jquery-3.6.4.min.js',
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',  # Используйте версию jQuery UI из того же источника
            'modeltranslation/js/tabbed_translation_fields.js',
        ]
        css = {
            'screen': ['modeltranslation/css/tabbed_translation_fields.css'],
        }

