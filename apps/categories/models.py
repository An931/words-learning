from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name=_('Name'),
    )
    icon = models.URLField(
        # todo check what is it in admin
        verbose_name=_('Icon'),
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
