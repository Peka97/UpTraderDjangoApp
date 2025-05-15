from django.db import models


class Menu(models.Model):
    """Меню"""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название меню')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Пункт меню"""
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Меню')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        verbose_name='Родительский пункт')
    title = models.CharField(max_length=100, verbose_name='Название пункта')
    url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='URL')
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text="Порядок сортировки пунктов меню. По умолчанию 0"
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        return self.url or '/'
