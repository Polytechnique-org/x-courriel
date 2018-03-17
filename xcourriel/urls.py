from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'xcourriel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    url(r'^$', TemplateView.as_view(template_name='simple.html')),
]
