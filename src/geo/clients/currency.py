"""
Функции для взаимодействия с внешним сервисом-провайдером данных о курсах валют.
"""
from http import HTTPStatus
from typing import Optional

import httpx

from app.settings import REQUESTS_TIMEOUT, API_KEY_APILAYER
from base.clients.base import BaseClient
from geo.clients.shemas import CurrencyRatesDTO


class CurrencyClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о курсах валют.
    """

    def get_base_url(self) -> str:
        return "https://api.apilayer.com/fixer/latest"

    def _request(self, endpoint: str) -> Optional[dict]:

        # формирование заголовков запроса
        headers = {"apikey": API_KEY_APILAYER}

        with httpx.Client(timeout=REQUESTS_TIMEOUT) as client:
            # получение ответа
            response = client.get(endpoint, headers=headers)
            if response.status_code == HTTPStatus.OK:
                return response.json()

            return None

    def get_rates(self, base: str = "rub") -> CurrencyRatesDTO | None:
        """
        Получение данных о курсах валют.

        :param base: Базовая валюта
        :return:
        """

        data = self._request(f"{self.get_base_url()}?base={base}")
        if not data:
            return None
        return CurrencyRatesDTO(
            base=data["base"], date=data["date"], rates=data["rates"]
        )
