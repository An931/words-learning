from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):

    name = models.CharField()
    translation = models.CharField()

    def __str__(self):
        return f'{self.name} - {self.translation}'

    class Meta:
        db_table = 'words'
        ordering = ('name',)
        verbose_name = _('Word')
        verbose_name_plural = _('Words')


