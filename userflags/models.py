from django.db import models

from django.contrib.auth.models import User


class FlagMananager(models.Manager):
    def for_user(self, user):
        return user.flag_set.all()


class Flag(models.Model):
    users = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=255)

    objects = FlagMananager()

    def __unicode__(self):
        return self.name

    def add_user(self, user):
        if not self.has_user(user):
            try:
                self.users.add(user)
            except Exception, e:
                if not self.has_user(user):
                    raise e
            else:
                self.save()

    def remove_user(self, user):
        if self.has_user(user):
            self.users.remove(user)
            self.save()

    def has_user(self, user):
        try:
            self.users.get(id=user.id)
        except User.DoesNotExist:
            return False
        else:
            return True
