from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import src.accounts.urls
import src.blocks.urls
import src.comments.urls
import src.config.urls
import src.recipes.urls
from src.authentication.views.login import LoginView

API_PREFIX = 'api/'

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name='login'),
    path(API_PREFIX, include(src.accounts.urls)),
    path(API_PREFIX, include(src.blocks.urls)),
    path(API_PREFIX, include(src.comments.urls)),
    path(API_PREFIX, include(src.config.urls)),
    path(API_PREFIX, include(src.recipes.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
