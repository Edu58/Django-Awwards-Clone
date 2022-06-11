import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('vote/<int:project_id>/', views.vote, name='vote'),
    path('rate/<int:project_id>/', views.rate_project, name='rate')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
