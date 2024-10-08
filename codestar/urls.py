from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include("news.urls"), name='news-urls'),
]


handler404 = 'codestar.views.handler404'
handler500 = 'codestar.views.handler500'
handler403 = 'codestar.views.handler403'
handler405 = 'codestar.views.handler405'