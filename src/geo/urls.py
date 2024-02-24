from django.urls import path

from geo.views import (
    get_city,
    get_cities,
    get_countries,
    get_country,
    get_weather,
    get_currency,
)

urlpatterns = [
    path("city", get_cities, name="cities"),
    path("city/<str:name>", get_city, name="city"),
    path("country", get_countries, name="countries"),
    path("country/<str:name>", get_country, name="country"),
    path("weather/<str:alpha2code>/<str:city>", get_weather, name="weather"),
    path("currency/<str:currency_base>", get_currency, name="currency"),
]
