from django.db import models
from django.utils.translation import ugettext_lazy as _


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
        # todo what if double name
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
