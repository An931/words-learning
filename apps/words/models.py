from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name='Name',
    )
    translation = models.CharField(
        max_length=20,
        verbose_name='Translation',
    )
    transcription = models.CharField(
        max_length=30,
        verbose_name='Transcription',
    )
    example = models.CharField(
        # char or text todo
        max_length=255,
        verbose_name='Phrase example'
    )
    sound = models.URLField(
        verbose_name='Sound',
    )
    picture = models.URLField(
        verbose_name='Picture',
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


