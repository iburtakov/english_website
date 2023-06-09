"""proj_english URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('terms-list', views.terms_list),
    path('add-term', views.add_term),
    path('send-term', views.send_term_to_check),
    path('terms-use', views.terms_use),
    path('add-note', views.add_note),
    path('notes', views.show_notes),
    path('check-term', views.check_term),
    path('send-note', views.send_note),
    path('grammar-use', views.grammar_use),
    path('check-grammar', views.check_grammar)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
