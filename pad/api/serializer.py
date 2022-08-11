from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):

    '''Note Model serializer class.'''

    class Meta:
        model = Note
        fields = ('created', 'name', 'content')
