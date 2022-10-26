import datetime
from django.db import models


class City(models.Model):
    """
    • Название
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"


class Street(models.Model):
    """
    • Название
    • Город
    """

    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, verbose_name="City", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city})"

    class Meta:
        verbose_name = "Street"


class Shop(models.Model):
    """
    • Название
    • Город
    • Улица
    • Дом
    • Время открытия
    • Время закрытия
    """

    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=5)  # Выбран Char поскольку номер дома может содержать литерал
    opening = models.TimeField(default=datetime.time(8, 00))
    closing = models.TimeField(default=datetime.time(20, 00))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shop"
