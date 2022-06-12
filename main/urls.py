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
    path('rate/<int:project_id>/', views.rate_project, name='rate'),
    path('profile/<username>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
