import imp
from re import I
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Awwards API')

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('vote/<int:project_id>/', views.vote, name='vote'),
    path('rate/<int:project_id>/', views.rate_project, name='rate'),
    path('profile/<username>/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('api/profiles/', views.ProfilesListView.as_view()),
    path('api/projects/', views.ProjectsListView.as_view()),
    path("api/token/", obtain_auth_token),
    path('swagger/', schema_view),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
