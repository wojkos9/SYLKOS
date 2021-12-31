"""Sylkos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

from django.conf.urls.static import static
from django.conf import settings

# form e-mail verification
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    path('admin/', admin.site.urls),

    # custom version of the registration view
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/"
         ),
         name="django_registration_register"),


    path("accounts/",
         include("django_registration.backends.one_step.urls")),

    # login via browser
    path("accounts/",
         include("django.contrib.auth.urls")),

    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path("api/",
         include("users.api.urls")),

    path("api/",
         include("voting.api.urls")),

    # login via browsable api
    path("api-auth/",
         include("rest_framework.urls")),

    # login via rest
    path("api/rest-auth/",
         include("rest_auth.urls")),

    # registration via rest
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),

    re_path(r"^$", IndexTemplateView.as_view(), name="entry-point")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)