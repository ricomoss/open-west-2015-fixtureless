import random
import itertools

from fixtureless import Factory
from django.core.management.base import BaseCommand

from owc_fixtureless import models


class Command(BaseCommand):
    help = 'Populate the local DB with development data.'
    args = '<mage count> <unicorn count>'

    def __init__(self):
        models.Mage.objects.all().delete()
        models.Unicorn.objects.all().delete()
        self.factory = Factory()
        super().__init__()

    def _generate_mages(self, mage_count):
        mage_names = ['rose', 'henry', 'alex', 'erica', 'ashley', 'bob', 'ted']
        initial_list = list()
        for _ in itertools.repeat(None, mage_count):
            initial_list.append({
                'name': random.choice(mage_names)
            })
        self.factory.create(models.Mage, initial_list)

    def _generate_unicorns(self, unicorn_count):
        unicorn_names = ['charlie', 'stephanie', 'shannon', 'pat', 'brian']
        initial_list = list()
        for _ in itertools.repeat(None, unicorn_count):
            initial_list.append({
                'name': random.choice(unicorn_names),
                'age': random.randint(1, 50),
                'best_friend': random.choice(models.Mage.objects.all())
            })
        self.factory.create(models.Unicorn, initial_list)

    def handle(self, *args, **options):
        if len(args) < 2:
            print(self.usage('./manage.py generate_dev_data'))
            return

        mage_count = int(args[0])
        unicorn_count = int(args[1])
        self._generate_mages(mage_count)
        self._generate_unicorns(unicorn_count)
