from django.contrib import admin
from .models import (
    About, Contact, WhatWeDo, OurTeam, Partners, Gallery,
    State, LocalGovernment, PlacesImpacted,
    InnovativeAgriculturalPractices, Transformation
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "description")
    search_fields = ("description",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "service")
    search_fields = ("full_name", "email", "phone", "service")


@admin.register(WhatWeDo)
class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "file", "is_video")
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    search_fields = ("name", "abbreviation")


@admin.register(LocalGovernment)
class LocalGovernmentAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    search_fields = ("name",)
    list_filter = ("state",)


@admin.register(PlacesImpacted)
class PlacesImpactedAdmin(admin.ModelAdmin):
    list_display = ("state", "local_government", "file")
    search_fields = ("state__name", "local_government__name")
    list_filter = ("state",)


@admin.register(InnovativeAgriculturalPractices)
class InnovativeAgriculturalPracticesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Transformation)
class TransformationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.site_header = "Noma Admin Dashboard"
admin.site.site_title = "Noma Portal"
admin.site.index_title = "Welcome to Noma Administration"
