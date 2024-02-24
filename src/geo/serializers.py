from rest_framework import serializers

from geo.models import Country, City, Weather, Currency, CurrencyRates


class CountrySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о стране.
    """

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "alpha2code",
            "alpha3code",
            "capital",
            "region",
            "subregion",
            "population",
            "latitude",
            "longitude",
            "demonym",
            "area",
            "numeric_code",
            "flag",
            "currencies",
            "languages",
        ]


class CitySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о городе.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "region",
            "latitude",
            "longitude",
            "country",
        ]


class WeatherSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о погоде.
    """

    city = CitySerializer(read_only=True)

    class Meta:
        model = Weather
        fields = [
            "id",
            "temp",
            "pressure",
            "humidity",
            "wind_speed",
            "description",
            "visibility",
            "dt",
            "timezone",
            "city",
        ]


class CurrencySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о валюте.
    """

    class Meta:
        model = Currency
        fields = [
            "id",
            "base",
            "date",
        ]


class CurrencyRatesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о курсе валют.
    """

    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = CurrencyRates
        fields = ["id", "currency_name", "rate", "currency"]
