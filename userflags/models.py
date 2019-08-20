from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class FlagManager(models.Manager):
    def for_user(self, user):
        return user.flag_set.all()


class Flag(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    name = models.CharField(max_length=255)

    objects = FlagManager()

    def __str__(self):
        return self.name

    @property
    def humanized(self):
        return self.name.replace('_', ' ').title()

    def add_user(self, user):
        if not self.has_user(user):
            try:
                self.users.add(user)
            except Exception as e:
                if not self.has_user(user):
                    raise e
            else:
                self.save()

    def remove_user(self, user):
        if self.has_user(user):
            self.users.remove(user)
            self.save()

    def has_user(self, user):
        User = get_user_model()
        try:
            self.users.get(id=user.id)
        except User.DoesNotExist:
            return False
        else:
            return True
