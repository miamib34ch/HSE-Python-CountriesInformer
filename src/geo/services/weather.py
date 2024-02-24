from typing import Optional
from django.db.models import Q

from geo.clients.shemas import WeatherInfoDTO
from geo.clients.weather import WeatherClient
from geo.models import Weather
from geo.services.city import CityService


class WeatherService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_weather(self, alpha2code: str, city: str) -> Optional[Weather]:
        """
        Получение погоды по стране и городу.

        :param alpha2code: ISO Alpha2 код страны
        :param city: Город
        :return:
        """

        weather = Weather.objects.filter(
            Q(city__name__contains=city)
            | Q(city__country__alpha2code__contains=alpha2code)
        )
        if not weather:
            if weather_data := WeatherClient().get_weather(f"{city},{alpha2code}"):
                weather_object = self.build_model(weather_data, city)
                return weather_object

        return weather.first()

    def build_model(self, weather: WeatherInfoDTO, city_name: str) -> Weather:
        """
        Формирование объекта модели погоды.

        :param WeatherInfoDTO weather: Данные о погоде.
        :param str city_name: Город
        :return:
        """

        city = CityService().get_cities(city_name)[:1][0]
        weather_object = Weather.objects.create(
            city=city,
            temp=weather.temp,
            pressure=weather.pressure,
            humidity=weather.humidity,
            wind_speed=weather.wind_speed,
            description=weather.description,
            visibility=weather.visibility,
            dt=weather.dt,
            timezone=weather.timezone,
        )
        return weather_object
