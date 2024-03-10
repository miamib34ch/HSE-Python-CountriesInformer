from rest_framework import serializers

from geo.serializers import CountrySerializer
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о новостях.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "source",
            "author",
            "title",
            "description",
            "url",
            "published_at",
            "country",
        ]
        ordering = ("published_at",)
