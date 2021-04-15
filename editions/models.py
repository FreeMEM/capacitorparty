from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from defaults.models import BaseModel
from django.utils.html import mark_safe
from productions.models import Scener, Description, Production, Organizer


class Sponsor(BaseModel):
    name = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)


class Edition(BaseModel):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    published_productions = models.BooleanField(default=False)
    sponsors = models.ManyToManyField(Sponsor, blank=True)
    organizers = models.ManyToManyField(Organizer)
    # logo = models.ForeignKey(File, blank=True, null=True, on_delete=models.SET_NULL)
    logo = models.ImageField(upload_to="pictures", blank=True, null=True)
    location = HTMLField(blank=True, null=True)
    link_google_map = models.CharField(max_length=255, blank=True, null=True)

    # pictures = models.ManyToManyField(EditionPicture, blank=True)

    def pictures_tag(self):
        return mark_safe(
            '<img src="%s" width="150" height="150" />' % (self.pictures.img.url)
        )

    class Meta:
        ordering = ("-start",)

    def __str__(self):
        return "%s" % (self.name)


class EditionPicture(BaseModel):
    img = models.ImageField(upload_to="pictures")
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.img.url))

    def __str__(self):
        return "%s" % (self.img)


# for edition in Edition.objects.all():
#     for picture in edition.pictures.all():
#         print("%s %s" % (edition.name, picture.img.url))
