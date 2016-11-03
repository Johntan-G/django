"""cardiac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import physical_database.views as physical_view
import psychological_database.views as psychological_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^health/$',physical_view.health,name = 'health'),
    url(r'^psychology/$',psychological_view.psychology,name = 'psychology'),
    url(r'^project/$',physical_view.project,name = 'project'),`
]
