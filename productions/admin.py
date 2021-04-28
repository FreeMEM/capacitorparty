# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Models
from django.contrib.auth.models import User
from productions.models import (
    Production,
    ScenersGroup,
    Scener,
    Organizer,
    Role,
    OrganizerRole,
    Prize,
    Compo,
)

# Register your models here.


class ProductionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "production_type", "edition")


@admin.register(Scener)
class ScenerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "name",
    )
    list_display_links = ("id", "user")
    list_editable = ("name",)
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
        "name",
    )
    list_filter = ("created_at", "modified_at", "user__is_staff", "user__is_active")

    fieldsets = (
        (
            "Perfil",
            {
                "fields": (
                    ("user", "name"),
                    ("avatar"),
                    ("avatar_tag"),
                    ("roles"),
                    ("description"),
                    ("external_link"),
                ),
            },
        ),
        (
            "Metadata",
            {
                "fields": (("created_at", "modified_at"),),
            },
        ),
    )

    readonly_fields = ("created_at", "modified_at", "avatar_tag")


class ScenerInline(admin.StackedInline):
    """ Scener in-line admin for users """

    model = Scener
    can_delete = False
    verbose_name_plural = "sceners"


class UserAdmin(BaseUserAdmin):
    inlines = (ScenerInline,)
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )


admin.site.unregister(User)
admin.site.register(Production, ProductionAdmin)
admin.site.register(ScenersGroup)
# admin.site.register(Scener, ScenerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Organizer)
admin.site.register(Role)
admin.site.register(OrganizerRole)
admin.site.register(Prize)
admin.site.register(Compo)
