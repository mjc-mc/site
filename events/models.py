from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import utils


class Event_Family(models.Model):
    
    family = models.CharField("Famille d'événements", max_length=50, null=False,
                              blank=False, unique=True)
    folder = models.CharField("Folder", max_length=40, default="images/event_family/", null=True, blank=True, editable=False)
    image = models.ImageField("Image", upload_to=utils.upload_path_handler, blank=True, null=True)

    def __str__(self):
            return self.family
        
    class Meta:
        verbose_name = "Famille d'événements"
        verbose_name_plural = "1. Familles d'événements"


def upload_path_handler(instance, filename):
    return "images/events/{family}/{title}/{file}".format(family=slugify(instance.family), title=slugify(instance.title), file=utils.clean_filename(filename))

            
class Event(models.Model):
    
    family = models.ForeignKey(Event_Family,  related_name="Event",  on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField("Titre (nom)", max_length=100, null=False, blank=False)
    subtitle = models.CharField("Sous-titre",  max_length=100, null=False, blank=True)
    description = RichTextField("Description", null=True, blank=False)
    venue = models.CharField("Lieu(x)",  max_length=100, null=False, blank=False)
    date_and_time = models.CharField("Date(s) & Heure(s)",  max_length=200, null=True, blank=False)
    date_first_day = models.DateField("Commence le", null=True)
    date_last_day = models.DateField("Finit le ", null=True)
    image = models.ImageField("Image", upload_to=upload_path_handler, blank=True, null=True)
    notes = models.CharField("Notes",  max_length=100, null=False, blank=True)
    bubble_info = models.TextField("Bulle info", null=True, blank=True)
    contact = models.CharField("Personne à contacter",  max_length=100, null=True, blank=True)
    rate = models.CharField("Tarifs", max_length=100, null=True, blank=True)
    file = models.FileField("PDF", upload_to='files/events/', null=True, blank=True)
        
    def __str__(self):
        return '%s - %s - %s' % (self.family, self.title, self.date_first_day)
    
    class Meta:
        verbose_name = "Evénement"
        verbose_name_plural = "2. Evénements"
