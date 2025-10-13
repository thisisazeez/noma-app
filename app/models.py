from django.db import models
from django.core.exceptions import ValidationError

def validate_file_type(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov', '.avi', '.mkv']
    import os
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Only image and video files are allowed.")

# class Banner(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="banners/%Y/%m/%d/", blank=True)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.title


class About(models.Model):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class Contact(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    further_explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            self.full_name,
            self.phone,
            self.email,
            self.service,
            self.further_explanation,
        )


class WhatWeDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team/%Y/%m/%d/", blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Partners(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="partners/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="gallery/%Y/%m/%d/", validators=[validate_file_type], blank=True)

    def __str__(self):
        return self.title

    @property
    def is_video(self):
        video_exts = [".mp4", ".mov", ".avi", ".mkv"]
        import os
        ext = os.path.splitext(self.file.name)[1].lower()
        return ext in video_exts



class State(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class LocalGovernment(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="local_governments")

    def __str__(self):
        return f"{self.name} ({self.state.name})"


class PlacesImpacted(models.Model):
    file = models.FileField(upload_to="places_impacted/%Y/%m/%d/", blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="places_impacted")
    local_government = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE, related_name="places_impacted")

    def is_video(self):
        if self.file:
            return self.file.name.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))
        return False

    def __str__(self):
        return f"{self.local_government.name}, {self.state.name}"



class InnovativeAgriculturalPractices(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="places_impacted/%Y/%m/%d/", blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transformation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
