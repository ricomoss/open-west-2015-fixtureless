from django.db import models

from owc_fixtureless import constants


class Mage(models.Model):
    name = models.CharField(max_length=40)
    magic_type = models.CharField(
        max_length=255, choices=constants.MAGIC_CHOICES)

    @property
    def brothers_in_arms(self):
        """
        Return a QuerySet object containing all other the mages who share the
        same magic_type as this mage.
        :return: QuerySet
        """
        return Mage.objects.filter(magic_type=self.magic_type).exclude(
            pk=self.pk)


class Unicorn(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    best_friend = models.ForeignKey(Mage)

    @property
    def details(self):
        return {
            'name': self.name,
            'age': self.age
        }
