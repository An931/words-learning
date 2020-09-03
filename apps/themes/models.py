from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _


class Theme(models.Model):
    """Theme model"""

    name = models.CharField(
        _('Name'),
        max_length=50,
    )
    translation = models.CharField(
        _('Translation'),
        max_length=50,
        blank=True,
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='category',
    )
    level = models.ForeignKey(
        'levels.Level',
        on_delete=models.SET_NULL,
        null=True,
        related_name='level',
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='static/images',
        null=True,
        blank=True,
    )

    @property
    def photo_preview(self):
        # todo move to admin model
        return mark_safe(f'<img src="{self.photo.url}" height="200"/>')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'themes'
        ordering = ('level', 'name')
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')
