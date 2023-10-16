import datetime
from django.db import models


class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(verbose_name='Время создания', default=datetime.datetime.now())
    deadline = models.DateField(null=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.deadline
