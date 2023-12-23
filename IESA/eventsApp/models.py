from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    responsible_person = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='event_photos/', blank=True, null=True)
    items_to_bring = models.TextField(blank=True, null=True)
    participation_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"/// {self.name} {self.category}  {self.date} - {self.time} ///"


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, help_text=_("Enter your first name."))
    last_name = models.CharField(max_length=255, help_text=_("Enter your last name."))
    email = models.EmailField(help_text=_("Enter a valid email address."))
    phone_number = models.CharField(max_length=20, help_text=_("Enter a valid phone number containing only digits."))
    date_of_birth = models.DateField(help_text=_("Enter your date of birth."))

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.date_of_birth} - {self.event}"
