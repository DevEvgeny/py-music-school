from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    model = Musician
    fields = (
        "id",
        "first_name",
        "last_name",
        "instrument",
        "age",
        "date_of_applying",
        "is_adult"
    )
