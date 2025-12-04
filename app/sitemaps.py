"""
Django Sitemaps Configuration for Noma App

Provides XML sitemap generation for search engine crawlers.
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """
    Sitemap for static pages of the Noma website.
    """
    protocol = 'https'
    changefreq = 'weekly'
    
    def items(self):
        """Return list of URL names for static pages."""
        return [
            'index',
            'about_us',
            'contact_us',
            'team',
            'our_work',
            'gallery',
            'places_impacted',
            'iap',
        ]
    
    def location(self, item):
        """Return the URL for each item."""
        return reverse(item)
    
    def priority(self, item):
        """
        Return priority for each page.
        Homepage gets highest priority.
        """
        priorities = {
            'index': 1.0,
            'about_us': 0.8,
            'contact_us': 0.8,
            'our_work': 0.7,
            'team': 0.6,
            'gallery': 0.6,
            'places_impacted': 0.6,
            'iap': 0.6,
        }
        return priorities.get(item, 0.5)


# Sitemap dictionary for URL configuration
sitemaps = {
    'static': StaticViewSitemap,
}
