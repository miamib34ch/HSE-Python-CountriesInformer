from django.db import models

from base.models import TimeStampMixin
from geo.models import Country


class News(TimeStampMixin):
    """Модель для новостей"""

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        related_name="news_country",
        verbose_name="Страна",
    )
    source = models.CharField(max_length=50, verbose_name="Источник")
    author = models.CharField(
        max_length=500,
        default="",
        blank=True,
        verbose_name="Автор",
    )
    title = models.CharField(
        max_length=500,
        verbose_name="Заголовок",
    )
    description = models.TextField(
        default="",
        blank=True,
        verbose_name="Описание",
    )
    url = models.CharField(
        max_length=500,
        default="",
        blank=True,
        verbose_name="Ссылка на источник",
    )
    published_at = models.DateTimeField(
        verbose_name="Дата и время публикации",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["published_at"]
