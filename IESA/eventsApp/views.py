from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Participant
from .forms import EventsRegistrationForm


def event_list(request):
    events = Event.objects.all()
    eventsRegistrationForm = EventsRegistrationForm()

    return render(request, 'eventsApp/event_list.html',
                  {'events': events, 'eventsRegistrationForm': eventsRegistrationForm})


def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    eventsRegistrationForm = EventsRegistrationForm()

    if request.method == 'POST':
        eventsRegistrationForm = EventsRegistrationForm(request.POST)
        if eventsRegistrationForm.is_valid():
            participant = eventsRegistrationForm.save(commit=False)
            participant.event = event
            participant.save()

            # Дополнительные действия в случае успешной регистрации
            messages.success(request, 'Registration successful!')
            return redirect('eventsApp:event_list')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
            print(eventsRegistrationForm.errors)  # Add this line to print form errors

    # Если форма не прошла валидацию или это GET-запрос, отображаем страницу события с формой
    return render(request, 'eventsApp/event_list.html',
                  {'event': event, 'eventsRegistrationForm': eventsRegistrationForm})
