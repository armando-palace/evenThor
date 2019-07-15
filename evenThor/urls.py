"""evenThor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from meeting import views as v
"""from meeting.views import  SignInView, SignOutView"""

urlpatterns = [
  path('meeting/', include('meeting.urls')),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  url(r'^$', v.index, name='index'),
  url(r'^incia-sesion/$', v.SignInView.as_view(), name='sign_in'),
  url(r'^cerrar-sesion/$', v.SignOutView.as_view(), name='sign_out'),
  url(r'^home/$', v.home, name='home'),
  url(r'^home-admin/$', v.home_admin, name='home_admin'),
  url(r'^home-manager/$', v.home_manager, name='home_manager'),
  url(r'^home-agent/$', v.home_agent, name='home_agent'),
]
