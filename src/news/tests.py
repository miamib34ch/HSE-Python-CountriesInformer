from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from geo.models import Country
from news.models import News


class NewsTestCase(APITestCase):
    """
    Тесты для новостей.
    """

    def setUp(self) -> None:
        """
        Подготовка данных для тестов.
        :return:
        """
        country = Country.objects.create(
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
        self.news = News.objects.create(
            country=country,
            source="test",
            author="test",
            title="test",
            description="test",
            url="test",
            published_at=datetime.now().astimezone(),
        )
        News.objects.create(
            country=country,
            source="test2",
            author="test2",
            title="test2",
            description="test2",
            url="test2",
            published_at=datetime.now().astimezone(),
        )

    def test_get_news(self) -> None:
        """
        Тест получения новостей.
        :return:
        """
        response = self.client.get(reverse("news", kwargs={"alpha2code": "te"}))
        data = response.json()["results"]
        item = data[0]
        self.assertEqual(len(data), 1)
        self.assertEqual(item["source"], self.news.source)
        self.assertEqual(item["author"], self.news.author)
        self.assertEqual(item["title"], self.news.title)
        self.assertEqual(item["description"], self.news.description)
