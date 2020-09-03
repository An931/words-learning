from django.db import models
# from audiofield.fields import AudioField
from django.utils.html import format_html, mark_safe
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Word(models.Model):
    """Word model"""

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
        return format_html(
            f'<a href="{self.picture.url}"> <img src="{self.picture.url}" height="200"/></a>')

    # mb add link

    # picture_preview.short_description = _('Audio file player')  #todo for all and change

    # @property
    def sound_preview(self):
        return format_html(f'<audio controls src="{self.sound.url}"></audio>')
        # return format_html(f'<img src="{self.sound.url}"/>')
        # return mark_safe(f'<audio src="{self.sound.url}" autoplay></audio>')

    # todo in admin only, not in model

    def clean(self):
        """Check if sound field has right extension"""
        #     todo is it need to check img?
        # maybe check name symbols for all
        if self.sound and not self.sound.name.endswith('.mp3'):
            raise ValidationError(
                {'sound': _('File should have mp3 extension')})

    def __str__(self):
        return f'{self.name} - {self.translation}'

    class Meta:
        db_table = 'words'
        ordering = ('name',)
        verbose_name = _('Word')
        verbose_name_plural = _('Words')
