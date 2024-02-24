"""
Функции для взаимодействия с внешним сервисом-провайдером данных о погоде.
"""
from http import HTTPStatus
from typing import Optional

import httpx

from app.settings import REQUESTS_TIMEOUT, API_KEY_OPENWEATHER
from base.clients.base import BaseClient
from geo.clients.shemas import WeatherInfoDTO


class WeatherClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о погоде.
    """

    def get_base_url(self) -> str:
        return "https://api.openweathermap.org/data/2.5/weather"

    def _request(self, endpoint: str) -> Optional[dict]:
        with httpx.Client(timeout=REQUESTS_TIMEOUT) as client:
            # получение ответа
            response = client.get(endpoint)
            if response.status_code == HTTPStatus.OK:
                return response.json()

            return None

    def get_weather(self, location: str) -> Optional[WeatherInfoDTO]:
        """
        Получение данных о погоде.

        :param location: Город и страна
        :return:
        """

        data = self._request(
            f"{self.get_base_url()}?units=metric&q={location}&appid={API_KEY_OPENWEATHER}"
        )

        return (
            WeatherInfoDTO(
                temp=data["main"]["temp"],
                pressure=data["main"]["pressure"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                description=data["weather"][0]["description"],
                visibility=data["visibility"],
                dt=data["dt"],
                timezone=data["timezone"] // 3600,
            )
            if data
            else None
        )
