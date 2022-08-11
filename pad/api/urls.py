'''API urls defined for views.'''

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('notes/', views.ListNoteView.as_view(),
        name='apinotes'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
