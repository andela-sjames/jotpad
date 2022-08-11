from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.generics import ListCreateAPIView

from api.models import Note
from api.serializer import NoteSerializer
from api.setpagination import LimitOffsetpage

from rest_framework.response import Response

from rest_framework import filters


from rest_framework.schemas.openapi import AutoSchema


# Create your views here.
class HomeView(TemplateView):
    """Homepage View defined here."""

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class ListNoteView(ListCreateAPIView):
    """
    List all Notes, or create a new Note.
    """
    queryset = Note.objects.all()
    model = Note
    serializer_class = NoteSerializer
    pagination_class = LimitOffsetpage
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
