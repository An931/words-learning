from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe


class Category(models.Model):
    """Category model"""

    name = models.CharField(
        _('Name'),
        max_length=50,
        unique=True,
    )
    translation = models.CharField(
        _('Translation'),
        max_length=50,
        blank=True,
    )
    icon = models.ImageField(
        _('Icon'),
        upload_to='static/images',
        # todo what is double name
        null=True,
        blank=True,
    )

    @property
    def icon_preview(self):
        return mark_safe(f'<img src="{self.icon.url}" height="200"/>')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
