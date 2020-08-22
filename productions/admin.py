from django.contrib import admin
from productions.models import Production, ScenersGroup, Scener, Organizer, Role, OrganizerRole, Prize, Compo, File

# Register your models here.

class ProductionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "production_type","edition")


admin.site.register(Production, ProductionAdmin)
admin.site.register(ScenersGroup)
admin.site.register(Scener)
admin.site.register(Organizer)
admin.site.register(File)
admin.site.register(Role)
admin.site.register(OrganizerRole)
admin.site.register(Prize)
admin.site.register(Compo)
