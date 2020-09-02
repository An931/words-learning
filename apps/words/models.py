from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=20,
    )
    plural = models.CharField(
        _('Plural'),
        max_length=20,
        blank=True,
    )
    translation = models.CharField(
        _('Translation'),
        max_length=20,
    )
    transcription = models.CharField(
        _('Transcription'),
        max_length=30,
        blank=True,
    )
    example = models.CharField(
        _('Phrase example'),
        max_length=255,
        blank=True,
    )
    sound = models.URLField(
        _('Sound'),
        blank=True,
    )
    picture = models.URLField(
        _('Picture'),
        blank=True,
    )
    theme = models.ForeignKey(
        'themes.Theme',
        on_delete=models.CASCADE,
        related_name='theme',
    )

    def __str__(self):
        return f'{self.name} - {self.translation}'

    class Meta:
        db_table = 'words'
        ordering = ('name',)
        verbose_name = _('Word')
        verbose_name_plural = _('Words')


