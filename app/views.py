from django.shortcuts import render, redirect
from .models import (
    OurTeam,
    About,
    Partners,
    WhatWeDo,
    Contact,
    Gallery,
    Transformation,
    InnovativeAgriculturalPractices,
    State,
)
from django.contrib import messages


def index(request):
    whatwedo = WhatWeDo.objects.all()
    partners = Partners.objects.all()

    context = {
        "whatwedo": whatwedo,
        "partners": partners,
    }
    return render(request, "index.html", context)


def about_us(request):
    about = About.objects.first()

    partners = Partners.objects.all()

    return render(request, "about-us.html", {"about": about, "partners": partners})


def team_view(request):
    """
    Render the team page with all OurTeam objects.
    """
    team_members = OurTeam.objects.all()
    return render(request, "team.html", {"team_members": team_members})


def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("Phone")
        service = request.POST.get("service")
        further_explanation = request.POST.get("further_explanation")

        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            service=service,
            further_explanation=further_explanation,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact_us")

    return render(request, "contact-us.html")


def gallery_view(request):
    gallery_items = Gallery.objects.all()

    context = {
        "gallery_items": gallery_items,
    }

    return render(request, "masonery.html", context)


def transformation_view(request):
    transformations = Transformation.objects.all()
    return render(request, "our-work.html", {"transformations": transformations})


def coming_soon(request):
    return render(request, "coming-soon.html")


def iap_view(request):
    iap_items = InnovativeAgriculturalPractices.objects.all()
    return render(request, "iap.html", {"iap_items": iap_items})


def places_impacted(request):
    states = State.objects.prefetch_related("local_governments__places_impacted").all()
    return render(request, "places-impacted.html", {"states": states})


def robots_txt(request):
    """
    Serve robots.txt file for search engine crawlers.
    """
    from django.http import HttpResponse
    
    content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://nomanigeria.com/sitemap.xml

# Crawl-delay
Crawl-delay: 1
"""
    return HttpResponse(content, content_type="text/plain")

