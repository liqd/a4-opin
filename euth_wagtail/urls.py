from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps import views as wagtail_sitemap_views
from wagtail.contrib.sitemaps.sitemap_generator import \
    Sitemap as WagtailSitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from adhocracy4.api import routers as a4routers
from adhocracy4.comments_async.api import CommentViewSet
from adhocracy4.polls.api import PollViewSet
from adhocracy4.polls.api import VoteViewSet
from adhocracy4.polls.routers import QuestionDefaultRouter
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from euth.accounts import urls as accounts_urls
from euth.blueprints import urls as blueprints_urls
from euth.communitydebate import urls as communitydebate_urls
from euth.contrib.sitemaps.adhocracy4_sitemap import Adhocracy4Sitemap
from euth.contrib.sitemaps.static_sitemap import StaticSitemap
from euth.dashboard import urls as dashboard_urls
from euth.documents import urls as paragraph_urls
from euth.documents.api import DocumentViewSet
from euth.follows.api import FollowViewSet
from euth.ideas import urls as ideas_urls
from euth.maps import urls as maps_urls
from euth.memberships import projects_urls as memberships_project_urls
from euth.memberships import urls as memberships_urls
from euth.offlinephases import urls as offlinephases_urls
from euth.organisations import urls as organisations_urls
from euth.projects import urls as project_urls
from euth.projects.api import ProjectViewSet
from euth.users import urls as user_urls
from euth.users.api import UserViewSet

from . import urls_accounts

router = routers.DefaultRouter()
router.register(r'follows', FollowViewSet, basename='follows')
router.register(r'polls', PollViewSet, basename='polls')
router.register(r'reports', ReportViewSet, basename='reports')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'users', UserViewSet, basename='users')

question_router = QuestionDefaultRouter()
question_router.register(r'vote', VoteViewSet, basename='vote')

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, basename='comments')
ct_router.register(r'ratings', RatingViewSet, basename='ratings')

module_router = a4routers.ModuleDefaultRouter()
module_router.register(r'documents', DocumentViewSet, basename='documents')

sitemaps = {
    'adhocracy4': Adhocracy4Sitemap,
    'wagtail': WagtailSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(ct_router.urls)),
    url(r'^api/', include(module_router.urls)),
    url(r'^api/', include(question_router.urls)),
    url(r'^upload/',
        login_required(ck_views.upload), name='ckeditor_upload'),
    url(r'^browse/',
        never_cache(login_required(ck_views.browse)), name='ckeditor_browse'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt',
        content_type="text/plain"), name="robots_file"),
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include(accounts_urls)),
    url(r'^dashboard/', include(dashboard_urls)),
    url(r'^profile/', include(user_urls)),
    url(r'^orgs/', include(organisations_urls)),
    url(r'^projects/', include(project_urls)),
    url(r'^projects/', include(memberships_project_urls)),
    url(r'^paragraphs/', include(paragraph_urls)),
    url(r'^offlineevents/', include(offlinephases_urls)),
    url(r'^ideas/', include(ideas_urls)),
    url(r'^maps/', include(maps_urls)),
    url(r'^memberships/', include(memberships_urls)),
    url(r'^blueprints/', include(blueprints_urls)),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^sitemap\.xml$',
        wagtail_sitemap_views.index,
        {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        wagtail_sitemap_views.sitemap,
        {'sitemaps': sitemaps}, name='sitemaps'),
    url(r'^communitydebate/', include(communitydebate_urls)),
    url(r'', include(wagtail_urls)),
)

urlpatterns += [
    url(r'^accounts/', include(urls_accounts)),
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
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
