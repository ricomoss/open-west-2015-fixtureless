from django.test import TestCase
from fixtureless import Factory

from owc_fixtureless import constants
from owc_fixtureless import models


class MageTestCase(TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_brothers_in_arms(self):
        # Exclude the mage itself
        mage_1 = self.factory.create(
            models.Mage, {'magic_type': constants.ARCANE})
        expected = 0
        self.assertEqual(mage_1.brothers_in_arms.count(), expected)

        # Let's add another mage with another magic_type
        self.factory.create(models.Mage, {'magic_type': constants.BLACK})
        expected = 0
        self.assertEqual(mage_1.brothers_in_arms.count(), expected)

        # Let's add another mage with the same magic_type
        self.factory.create(models.Mage, {'magic_type': constants.ARCANE})
        expected = 1
        self.assertEqual(mage_1.brothers_in_arms.count(), expected)
