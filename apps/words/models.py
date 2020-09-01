from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):

    name = models.CharField(
        verbose_name='Name',
    )
    translation = models.CharField(
        verbose_name='Translation',
    )
    transcription = models.CharField(
        verbose_name='Transcription',
    )
    example = models.CharField(
        # char or text todo
        verbose_name='Phrase example'
    )
    sound = models.URLField(
        verbose_name='Sound',
    )
    picture = models.URLField(
        verbose_name='Picture',
    )
    theme = models.ForeignKey(
    #     todo
    #    todo or many to many
    )

    def __str__(self):
        return f'{self.name} - {self.translation}'

    class Meta:
        db_table = 'words'
        ordering = ('name',)
        verbose_name = _('Word')
        verbose_name_plural = _('Words')


