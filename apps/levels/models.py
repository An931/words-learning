from django.db import models
from django.utils.translation import ugettext_lazy as _


class Level(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name=_('Name'),
    )
    code = models.CharField(
        max_length=2,
        verbose_name=_('Code'),
    )

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        db_table = 'levels'
        ordering = ('code',)
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')
