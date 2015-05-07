import random
import itertools
from optparse import make_option

from fixtureless import Factory
from django.core.management.base import BaseCommand

from owc_fixtureless import models


class Command(BaseCommand):
    help = 'Populate the local DB with development data.'
    args = '<mage count> <unicorn count>'

    option_list = BaseCommand.option_list + (
        make_option(
            '--use_custom',
            action='store_true',
            default=False,
            help='Have django-fixtureless use custom values instead of '
                 'random data. (default=False)',
        ),
        make_option(
            '--mage_count',
            type='int',
            default=5,
            help='The number of mages you want in your system. (default=5)',
        ),
        make_option(
            '--unicorn_count',
            type='int',
            default=5,
            help='The number of unicorns you want in your system. (default=5)',
        ),
        make_option(
            '--clear_db',
            action='store_true',
            default=False,
            help='Clear the database to start fresh.',
        ),
    )

    MAGE_NAMES = ['rose', 'henry', 'alex', 'erica', 'ashley', 'bob', 'ted']
    UNICORN_NAMES = ['charlie', 'stephanie', 'shannon', 'pat', 'brian']

    def __init__(self):
        models.Mage.objects.all().delete()
        models.Unicorn.objects.all().delete()
        self.factory = Factory()
        super().__init__()

    def _generate_mages(self, mage_count):
        if self.use_custom:
            initial_list = list()
            for _ in itertools.repeat(None, mage_count):
                initial_list.append({
                    'name': random.choice(self.MAGE_NAMES)
                })
            self.factory.create(models.Mage, initial_list)
        else:
            self.factory.create(models.Mage, mage_count)

    def _generate_unicorns(self, unicorn_count):
        initial_list = list()
        for _ in itertools.repeat(None, unicorn_count):
            initial_dict = {
                'best_friend': random.choice(models.Mage.objects.all())
            }
            if self.use_custom:
                initial_dict['name']= random.choice(self.UNICORN_NAMES)
                initial_dict['age'] = random.randint(1, 50)
            initial_list.append(initial_dict)
        self.factory.create(models.Unicorn, initial_list)

    def handle(self, *args, **options):
        self.use_custom = options['use_custom']

        if options['clear_db']:
            return

        mage_count = options['mage_count']
        unicorn_count = options['unicorn_count']
        self._generate_mages(mage_count)
        self._generate_unicorns(unicorn_count)
