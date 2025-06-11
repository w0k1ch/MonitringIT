from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Ремонт_системы','Ремонт_системы'),
    ('Обновление_ПО','Обновление_ПО'),
    ('Диагностика','Диагностика'),
)

class Tasks(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20 ,choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Задача'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Execution(models.Model):
    Tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    execution_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Исполнение'

    def __str__(self):
        return f'{self.Tasks} исполняет {self.staff.username}'