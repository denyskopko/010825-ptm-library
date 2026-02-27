from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date


"""Обновите уже существующую модель Author дополнительными полями:
Профиль: ссылка на личную страницу автора, может быть не указана -
Удалён: поле, которое позволит смотреть удалён ли этот автор из базы всех авторов. 
По умолчанию все авторы активны
Рейтинг: позволит отсматривать рейтинг популярности авторов"""
# Create your models here.
class Author(models.Model):
    first_name : str = models.CharField(max_length=100)
    last_name : str = models.CharField(max_length=100)
    birth_date : date = models.DateField()
    profile : str = models.URLField( null=True, default='Null', max_length=100)
    remote : bool = models.BooleanField(default=False, null=True)
    rating : int = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])