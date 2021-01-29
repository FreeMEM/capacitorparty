from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from defaults.models import BaseModel
from embed_video.fields import EmbedVideoField

# Create your models here.


class Description(BaseModel):
    content = HTMLField()


class ProductionType(models.TextChoices):
    GRAPHICS = 1, 'Gráficos'
    MUSIC = 2, 'Música'
    DEMO = 3, 'Demo'
    INTRO = 4, 'Intro'
    PIXELART = 5, 'Pixel Art'
    WILDCOMPO = 6, 'Wild compo'
    GAMEDEV = 7, 'Game development'
    INVITATION = 8, 'Invitación'


class PrizeType(models.TextChoices):
    CASHPRIZE = 1, "Premio en metálico"
    GIFT = 2, "Regalo"
    COUPON = 3, 'Cupón'


class Role(BaseModel):
    name = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class OrganizerRole(BaseModel):
    name = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Scener(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    roles = models.ManyToManyField(Role)
    description = HTMLField(blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    # roll = models.CharField(
    #     max_length=2,
    #     choices=Roll.choices,
    #     default=Roll.CODER,
    # )


class Organizer(BaseModel):
    name = models.CharField(max_length=200)
    roles = models.ManyToManyField(OrganizerRole)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ScenersGroup(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    member = models.ManyToManyField(Scener)
    description = HTMLField(blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return '%s' % (self.name)


# class File(BaseModel):
#     name = models.CharField(max_length=200)
#     path = models.FileField(upload_to="files")
#     description = HTMLField(blank=True, null=True)

#     def __str__(self):
#         return '%s' % (self.name)

class Production(BaseModel):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)
    group = models.ForeignKey(ScenersGroup, blank=True, null=True, on_delete=models.SET_NULL)
    production_type = models.CharField(max_length=2,choices=ProductionType.choices, default=ProductionType.GRAPHICS)
    authors = models.ManyToManyField(Scener)
    date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # filepath = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)
    filepath = models.FileField(upload_to="files", blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    preview = models.ImageField(upload_to='pictures', blank=True, null=True)
    videolink = EmbedVideoField(max_length=200, blank=True, null=True)
    edition = models.ForeignKey('editions.Edition', blank=True, null=True, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]


class Prize(BaseModel):
    name = models.CharField(max_length=200)
    prize_type = models.CharField(max_length=2,choices=PrizeType.choices, default=PrizeType.CASHPRIZE)
    value = models.IntegerField(blank=False)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

class Compo(BaseModel):
    name = models.CharField(max_length=200)
    rules = HTMLField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)