from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db import models


class Swiper(models.Model):
    image = models.ImageField(upload_to="swiper_image/")

    def __str__(self):
        return f"{self.image}"
