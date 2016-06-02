from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from comments_api import urls as comments_api_urls

from search import views as search_views


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^api/', include(comments_api_urls)),
]

urlpatterns += i18n_patterns('',
    url(r'^adhocracy/', TemplateView.as_view(template_name="activate.html"), name="adhocracy"),
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
