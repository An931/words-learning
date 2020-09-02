from django.db import models
from django.utils.translation import ugettext_lazy as _


class Level(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=20,
        unique=True,
    )
    code = models.CharField(
        _('Code'),
        max_length=2,
        unique=True,
    )

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        db_table = 'levels'
        ordering = ('code',)
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')
