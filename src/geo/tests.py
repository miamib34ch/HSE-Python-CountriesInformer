from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from geo.models import City, Country, Currency, CurrencyRates, Weather


class CountryTestCase(APITestCase):
    """
    Тесты для сервиса стран.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.
        :return:
        """
        self.country = Country.objects.create(
            name="test",
            alpha2code="te",
            alpha3code="tes",
            capital="test",
            region="test",
            subregion="test",
            population=1,
            latitude=1,
            longitude=2,
            demonym="test",
            area=1,
            numeric_code=123,
            flag="test",
            currencies=[],
            languages=[],
        )
        self.city = City.objects.create(
            country=self.country,
            name="test",
            region="test",
            latitude=1,
            longitude=1,
        )
        self.weather = Weather.objects.create(
            city=self.city,
            temp=0,
            pressure=0,
            humidity=0,
            wind_speed=0,
            description="test",
            visibility=1,
            dt=datetime.now().astimezone(),
            timezone=1,
        )
        self.currency = Currency.objects.create(
            base="test", date=datetime.now().astimezone()
        )
        self.currency_rates_first = CurrencyRates.objects.create(
            currency=self.currency, currency_name="test", rate=2.0
        )
        self.currency_rates_second = CurrencyRates.objects.create(
            currency=self.currency, currency_name="test2", rate=0.5
        )

    def test_get_city(self) -> None:
        """
        Тест получения списка городов.
        :return:
        """
        response = self.client.get(reverse("cities"), {"codes": "te,test"})
        data = response.json()["results"]
        self.assertEqual(len(data), 1)
        item = data[0]
        self.assertEqual(item["name"], self.city.name)
        self.assertEqual(item["region"], self.city.region)

    def test_get_one_city(self) -> None:
        """
        Тест получения одного города.
        :return:
        """
        response = self.client.get(reverse("city", kwargs={"name": "test"}))
        data = response.json()["results"]
        item = data[0]
        self.assertEqual(item["name"], self.city.name)

    def test_get_countries(self) -> None:
        """
        Тест получения списка стран.
        :return:
        """
        response = self.client.get(reverse("countries"), {"codes": "te"})
        data = response.json()["results"]
        self.assertEqual(len(data), 1)
        item = data[0]
        self.assertEqual(item["name"], self.country.name)

    def test_get_one_countries(self) -> None:
        """
        Тест получения одной страны.
        :return:
        """
        response = self.client.get(reverse("country", kwargs={"name": "test"}))
        data = response.json()["results"][0]
        self.assertEqual(data["name"], self.country.name)

    def test_get_weather(self) -> None:
        """
        Тест получения погоды.
        :return:
        """
        response = self.client.get(
            reverse("weather", kwargs={"alpha2code": "te", "city": "test"})
        )
        item = response.json()
        self.assertEqual(item["temp"], self.weather.temp)
        self.assertEqual(item["pressure"], self.weather.pressure)
        self.assertEqual(item["humidity"], self.weather.humidity)
        self.assertEqual(item["wind_speed"], self.weather.wind_speed)
        self.assertEqual(item["description"], self.weather.description)

    def test_get_currency(self) -> None:
        """
        Тест получения валюты.
        :return:
        """
        data = self.client.get(
            reverse("currency", kwargs={"currency_base": "test"})
        ).json()["results"]
        self.assertEqual(len(data), 1)
        item = data[0]
        self.assertEqual(item["currency_name"], self.currency_rates_first.currency_name)
        self.assertEqual(item["rate"], self.currency_rates_first.rate)
