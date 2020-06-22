from django.contrib import admin
from editions.models import Edition, Sponsor, EditionPicture

# Register your models here.


class EditionPictureInline(admin.TabularInline):
    model = EditionPicture


class EditionAdmin(admin.ModelAdmin):
    list_display = ("id", "name","subtitle", "start")
    filter_horizontal = ('sponsors',)
    inlines = [EditionPictureInline,]
    # readonly_fields = ['pictures_tag']

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class EditionPictureAdmin(admin.ModelAdmin):
    # fields = ['image_tag']
    readonly_fields = ['image_tag']
    list_display = ['image_tag']
    

admin.site.register(Edition, EditionAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(EditionPicture, EditionPictureAdmin)