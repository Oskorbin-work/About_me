"""AA_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('base.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('user_profile.urls')),
    path('projects/sending_emails/', include('project_1_sending_emails.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----------------------------------------------------------------------------------------------------------------------
# HTTP STATUS

# Bad Request
handler400 = "base.views.custom_400"
# Unauthorized
handler401 = "base.views.custom_401"
# Forbidden
handler403 = "base.views.custom_403"
# Not Found
handler404 = 'base.views.custom_404'
# Internal Server Error
handler500 = "base.views.custom_500"
# Internal Server Error
handler502 = "base.views.custom_502"
# Service Unavailable
handler503 = "base.views.custom_503"
# Gateway Timeout
handler504 = "base.views.custom_504"
# ----------------------------------------------------------------------------------------------------------------------
