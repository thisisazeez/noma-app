"""
SEO Configuration and Utilities for Noma App

This module provides centralized SEO configuration and helper functions
for generating page-specific meta data.
"""

# Site-wide SEO defaults
SITE_NAME = "Noma - Produce Marketing Company"
SITE_DOMAIN = "nomanigeria.com"
SITE_URL = "https://nomanigeria.com"
DEFAULT_LOCALE = "en_NG"
DEFAULT_IMAGE = "/static/image/noma.jpeg"
DEFAULT_KEYWORDS = "agriculture, farming, Nigeria, smallholder farmers, agribusiness, produce marketing, mechanization, sustainable farming"

# Page-specific SEO configuration
SEO_CONFIG = {
    "index": {
        "title": "Noma - Produce Marketing Company | Empowering Nigerian Farmers",
        "description": "Noma empowers smallholder farmers in Nigeria through innovative agricultural practices, mechanized solutions, and direct market access. Transforming Nigerian agriculture since 2023.",
        "keywords": "Noma Nigeria, agricultural empowerment, smallholder farmers, pay with output model, Nigerian agribusiness, sustainable farming Nigeria",
        "og_type": "website",
    },
    "about_us": {
        "title": "About Us - Noma | Our Mission, Vision & Values",
        "description": "Learn about Noma's mission to empower Nigerian smallholder farmers through structured outgrower schemes, innovative practices, and sustainable agricultural development.",
        "keywords": "about Noma, Noma mission, Noma vision, Nigerian agriculture company, agricultural development Nigeria",
        "og_type": "website",
    },
    "contact_us": {
        "title": "Contact Us - Noma | Get in Touch for Agricultural Support",
        "description": "Contact Noma for agricultural support, mechanization services, fertilizer, extension services, and produce marketing. Located in Kano, Nigeria.",
        "keywords": "contact Noma, Noma Kano, agricultural support Nigeria, farming services contact",
        "og_type": "website",
    },
    "team": {
        "title": "Our Team - Noma | Meet the Agricultural Experts",
        "description": "Meet the dedicated team behind Noma's agricultural transformation. Our experts are committed to empowering Nigerian farmers and driving sustainable growth.",
        "keywords": "Noma team, agricultural experts Nigeria, Noma leadership, farming professionals",
        "og_type": "website",
    },
    "our_work": {
        "title": "Our Work - Noma | Driving Agricultural Transformation",
        "description": "Discover how Noma drives agricultural transformation in Nigeria through innovative practices, farmer empowerment, and sustainable development initiatives.",
        "keywords": "Noma work, agricultural transformation, farming innovation Nigeria, sustainable agriculture",
        "og_type": "website",
    },
    "gallery": {
        "title": "Gallery - Noma | Our Agricultural Impact in Pictures",
        "description": "View our gallery showcasing Noma's agricultural impact across Nigeria. See our farmers, projects, and transformation efforts in action.",
        "keywords": "Noma gallery, agricultural photos Nigeria, farming projects, farmer success stories",
        "og_type": "website",
    },
    "places_impacted": {
        "title": "Places Impacted - Noma | Communities We Serve",
        "description": "Explore the communities and regions across Nigeria where Noma has made a positive impact on smallholder farmers and agricultural practices.",
        "keywords": "Noma impact, communities served, Nigerian states, agricultural development regions",
        "og_type": "website",
    },
    "iap": {
        "title": "Innovative Agricultural Practices - Noma | Modern Farming Solutions",
        "description": "Learn about Noma's innovative agricultural practices including semi-mechanized farming, precision agriculture, and sustainable crop cultivation methods.",
        "keywords": "innovative agriculture, modern farming Nigeria, agricultural technology, precision farming, sustainable practices",
        "og_type": "website",
    },
    "coming_soon": {
        "title": "Market Hub - Noma | Coming Soon",
        "description": "Noma's Market Hub is coming soon. A platform connecting farmers directly to buyers at premium prices.",
        "keywords": "Noma market hub, agricultural marketplace, farmer market access",
        "og_type": "website",
    },
}


def get_seo_context(page_name, request=None):
    """
    Get the complete SEO context for a specific page.
    
    Args:
        page_name: The name of the page (must match keys in SEO_CONFIG)
        request: Optional Django request object for generating canonical URL
        
    Returns:
        dict: Complete SEO context including all meta tag values
    """
    config = SEO_CONFIG.get(page_name, {})
    
    # Build canonical URL
    canonical_url = SITE_URL
    if request:
        canonical_url = f"{SITE_URL}{request.path}"
    
    return {
        "seo_title": config.get("title", SITE_NAME),
        "seo_description": config.get("description", f"{SITE_NAME} - Empowering Nigerian smallholder farmers through innovative agricultural practices."),
        "seo_keywords": config.get("keywords", DEFAULT_KEYWORDS),
        "seo_image": f"{SITE_URL}{DEFAULT_IMAGE}",
        "seo_url": canonical_url,
        "seo_type": config.get("og_type", "website"),
        "seo_site_name": SITE_NAME,
        "seo_locale": DEFAULT_LOCALE,
        "seo_domain": SITE_DOMAIN,
    }


# Organization structured data (JSON-LD)
ORGANIZATION_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Noma - Produce Marketing Company",
    "alternateName": "NOMA",
    "url": SITE_URL,
    "logo": f"{SITE_URL}{DEFAULT_IMAGE}",
    "description": "Empowering Nigerian smallholder farmers through innovative agricultural practices and sustainable development.",
    "foundingDate": "2023",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "5th Floor African Alliance Building, F1 Sani Abacha Way, Airport Road",
        "addressLocality": "Kano",
        "addressRegion": "Kano State",
        "addressCountry": "NG"
    },
    "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+234-803-573-2567",
        "contactType": "customer service",
        "areaServed": "NG",
        "availableLanguage": ["en", "ha"]
    },
    "sameAs": []
}


# LocalBusiness structured data for contact page
LOCAL_BUSINESS_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Noma - Produce Marketing Company",
    "image": f"{SITE_URL}{DEFAULT_IMAGE}",
    "url": SITE_URL,
    "telephone": "+234-803-573-2567",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "5th Floor African Alliance Building, F1 Sani Abacha Way, Airport Road",
        "addressLocality": "Kano",
        "addressRegion": "Kano State",
        "postalCode": "",
        "addressCountry": "NG"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 12.0022,
        "longitude": 8.5919
    },
    "priceRange": "$$"
}
