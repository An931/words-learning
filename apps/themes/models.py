from django.db import models
from django.utils.translation import ugettext_lazy as _


class Theme(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name=_('Theme'),
    )
    category = models.ForeignKey(
        # todo
        'categories.Category',
        on_delete=models.CASCADE,  # todo chose the best
        related_name='category',
    )
    level = models.ForeignKey(
        'levels.Level',

        related_name='level',
    )
    photo = models.URLField(
        verbose_name='Photo'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'themes'
        ordering = ('level', 'name')
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')
