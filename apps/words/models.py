from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
# from audiofield.fields import AudioField

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
    sound = models.FileField(
        _('Sound'),
        # todo check extension
        upload_to='static/sounds',
        null=True,
        blank=True,
    )
    # sound = AudioField(
    #     _('Sound'),
    #     # todo check extension
    #     upload_to='static/sounds',
    #     null=True,
    #     blank=True,
    # )
    # ext_whitelist=(".mp3", ".wav", ".ogg"),
    #                         help_text=("Allowed type - .mp3, .wav, .ogg")
    picture = models.ImageField(
        _('Picture'),
        upload_to='static/images',
        null=True,
        blank=True,
    )
    theme = models.ForeignKey(
        'themes.Theme',
        on_delete=models.CASCADE,
        related_name='theme',
    )

    # @property
    def picture_preview(self):
        return mark_safe(f'<img src="{self.picture.url}" height="200"/>')

    # picture_preview.short_description = _('Audio file player')  #todo for all and change

    def __str__(self):
        return f'{self.name} - {self.translation}'

    class Meta:
        db_table = 'words'
        ordering = ('name',)
        verbose_name = _('Word')
        verbose_name_plural = _('Words')


