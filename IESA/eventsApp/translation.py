from modeltranslation.translator import TranslationOptions, translator
from .models import Event, Participant


class EventTranslationOptions(TranslationOptions):
    fields = ('name', 'organizer', 'responsible_person', 'location', 'category', 'description', 'items_to_bring')

# Проверяем, зарегистрирована ли модель Event для перевода
if not translator.get_options_for_model(Event):
    translator.register(Event, EventTranslationOptions)



class ParticipantTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)
if not translator.get_options_for_model(Participant):
    translator.register(Participant, ParticipantTranslationOptions)