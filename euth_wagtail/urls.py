from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps import views as wagtail_sitemap_views
from wagtail.contrib.sitemaps.sitemap_generator import \
    Sitemap as WagtailSitemap
from wagtail.documents import urls as wagtaildocs_urls

from adhocracy4.api import routers as a4routers
from adhocracy4.comments_async.api import CommentViewSet
from adhocracy4.polls.api import PollViewSet
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from euth.accounts import urls as accounts_urls
from euth.contrib.sitemaps.adhocracy4_sitemap import Adhocracy4Sitemap
from euth.contrib.sitemaps.static_sitemap import StaticSitemap

from . import urls_accounts

router = routers.DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register(r'reports', ReportViewSet, basename='reports')

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, basename='comments')
ct_router.register(r'ratings', RatingViewSet, basename='ratings')

module_router = a4routers.ModuleDefaultRouter()

sitemaps = {
    'adhocracy4': Adhocracy4Sitemap,
    'wagtail': WagtailSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('api/', include(router.urls)),
    path('api/', include(ct_router.urls)),
    path('api/', include(module_router.urls)),
    path('upload/', login_required(ck_views.upload), name='ckeditor_upload'),
    path('browse/',
         never_cache(login_required(ck_views.browse)), name='ckeditor_browse'),
    re_path(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt',
        content_type="text/plain"), name="robots_file"),
]

urlpatterns += i18n_patterns(
    path('accounts/', include(accounts_urls)),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    re_path(r'^sitemap\.xml$', wagtail_sitemap_views.index,
            {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$', wagtail_sitemap_views.sitemap,
            {'sitemaps': sitemaps}, name='sitemaps'),
    path('', include(wagtail_urls)),
)

urlpatterns += [
    path('accounts/', include(urls_accounts)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server

    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
