from django.contrib import admin

from geo.models import Country, City, Weather, Currency, CurrencyRates


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "alpha2code",
        "alpha3code",
        "numeric_code",
        "area",
        "population",
        "created_at",
        "updated_at",
    )

    search_fields = ("name", "alpha3code", "numeric_code")

    list_filter = (
        "created_at",
        "updated_at",
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "region",
        "created_at",
        "updated_at",
    )

    search_fields = ("name", "region")

    list_filter = (
        "created_at",
        "updated_at",
    )


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "temp",
        "pressure",
        "humidity",
        "wind_speed",
        "description",
        "visibility",
        "dt",
        "timezone",
        "created_at",
        "updated_at",
    )

    search_fields = ("city", "temp")

    list_filter = (
        "created_at",
        "updated_at",
    )


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "base",
        "date",
        "created_at",
        "updated_at",
    )

    search_fields = ("base", "date")

    list_filter = (
        "created_at",
        "updated_at",
    )


@admin.register(CurrencyRates)
class CurrencyRatesAdmin(admin.ModelAdmin):
    list_display = (
        "currency_name",
        "rate",
        "created_at",
        "updated_at",
    )

    search_fields = ("currency_name", "rate")

    list_filter = (
        "created_at",
        "updated_at",
    )
