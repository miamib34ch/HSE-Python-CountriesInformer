from typing import Optional, Dict

from django.db.models import Q, QuerySet

from geo.clients.currency import CurrencyClient
from geo.clients.shemas import CurrencyRatesDTO
from geo.models import Currency, CurrencyRates


class CurrencyService:
    """
    Сервис для работы с данными о валютах.
    """

    def get_currency(self, currency_base: str) -> Optional[dict]:
        """
        Получение валюты по названию.

        :param str currency_base: название валюты

        :return:
        """

        if data := CurrencyClient().get_rates(f"{currency_base}"):
            return data

        return None

    def build_model_rates(
        self, currency: Currency, name: str, rate: float
    ) -> CurrencyRates:
        """
        Формирование объекта модели значения отношений валют.

        :param Currency currency: Валюта
        :param str name: называние валюты
        :param float rate: отношение валют

        :return:
        """
        return CurrencyRates(
            currency=currency,
            currency_name=name,
            rate=rate,
        )

    def build_model(self, currency: CurrencyRatesDTO) -> Currency:
        """
        Формирование объекта модели валюты.

        :param CurrencyRatesDTO currency: Данные о валюте.

        :return:
        """

        return Currency(
            base=currency.base,
            date=currency.date,
        )