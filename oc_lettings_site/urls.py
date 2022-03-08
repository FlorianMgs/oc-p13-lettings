from django.contrib import admin
from django.urls import path, include
from home.views import index


def sentry_debug(request):
    return 0/2


urlpatterns = [
    path('', index, name='home'),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', sentry_debug)
]
