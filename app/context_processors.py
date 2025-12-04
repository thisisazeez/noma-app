"""
Django Context Processors for Noma App

Provides global template context variables for SEO and site-wide data.
"""

from .seo import SITE_URL, SITE_NAME, DEFAULT_IMAGE, ORGANIZATION_SCHEMA
import json


def seo_context(request):
    """
    Inject base SEO variables into every template context.
    
    Returns a dictionary with:
    - canonical_url: Full canonical URL for current page
    - site_url: Base site URL
    - site_name: Site name for meta tags
    - default_seo_image: Default Open Graph image
    - organization_schema: JSON-LD Organization markup
    """
    canonical_url = f"{SITE_URL}{request.path}"
    
    return {
        "canonical_url": canonical_url,
        "site_url": SITE_URL,
        "site_name": SITE_NAME,
        "default_seo_image": f"{SITE_URL}{DEFAULT_IMAGE}",
        "organization_schema_json": json.dumps(ORGANIZATION_SCHEMA, indent=2),
    }
