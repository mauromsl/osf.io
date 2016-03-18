from modularodm.exceptions import ValidationError

from tests.base import OsfTestCase
from website.addons.ubiquitypress.tests.factories import UbiquitypressSettingsFactory

class TestSettingsValidation(OsfTestCase):

	def setUp(self):
        super(TestSettingsValidation, self).setUp()
        self.settings = UbiquitypressSettingsFactory()

    def test_validate_journal_code(self):
        self.settings.journal_code = 'cg'
        try:
            self.settings.save()
        except ValidationError:
            assert 0
