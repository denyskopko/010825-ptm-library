from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

       
class Member(models.Model):
    first_name:str = models.CharField(max_length=50, verbose_name="Имя") 
    last_name:str = models.CharField(max_length=50, verbose_name="Фамилия") 
    email:str = models.EmailField(unique=True)
    gender:str = models.CharField(
        max_length=20,
        choices=[
            ('male','Мужской'),
            ('female','Женский'),
            ('other','Другой')
        ],
        verbose_name="Пол"
    )
    birth_date:date = models.DateField(verbose_name="Дата рождения")
    age:int = models.IntegerField(
        validators=[
            MinValueValidator(6),
            MaxValueValidator(120)
        ],
        verbose_name="Возраст"
    )
    role:str = models.CharField(
        max_length=20,
        choices=[
            ('admin','Админ'),
            ('staff','Сотрудник'),
            ('member','Читатель')
        ],
        verbose_name="Роль"
    )
    
    is_active:bool = models.BooleanField(default=True, verbose_name="Активный")
    
    libraries = models.ManyToManyField("Library", through="Membership", verbose_name="Библиотеки")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Membership(models.Model):
    member: 'Member' = models.ForeignKey(to='Member', on_delete=models.CASCADE)
    library: 'Library' = models.ForeignKey(to='Library', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('member','library')
    
    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.library.name}"
    
    
   