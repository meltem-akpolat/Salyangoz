# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


####    User    ####

class User(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=250)
    content = models.URLField(verbose_name=_('Content'), max_length=1024)
    time = models.DateTimeField(verbose_name=_('Time'), auto_now=False, auto_now_add=True)
    counter = models.IntegerField(verbose_name=_('Counter'), default=0)
    user_name = models.CharField(verbose_name=_('User Name'), max_length=100)
    photo = models.URLField(verbose_name=_('Photo'), max_length=1024)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.title
