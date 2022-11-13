from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в соц сети',
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )

    def __str__(self) -> str:
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Massage(models.Model):
    profile = models.ForeignKey(
        to = 'tgc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текс',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f'Сообщение от {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'