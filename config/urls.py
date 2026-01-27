"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mysite.urls")),
    path("o/", include(oauth2_urls)),
]


api_urlpatterns = [
    path("api/", include("api.urls")),
]

api_docs_urlpatterns = [
    path(
        "api/schema/",
        SpectacularAPIView.as_view(urlconf=api_urlpatterns),
        name="api_schema",
    ),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="api_schema"),
        name="api_swagger-ui",
    ),
]

urlpatterns += api_urlpatterns
urlpatterns += api_docs_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
