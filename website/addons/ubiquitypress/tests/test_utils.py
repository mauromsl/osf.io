from nose.tools import *  # PEP8 asserts

from tests.base import OsfTestCase

from website.addons.forward.tests.factories import UbiquitypressSettingsFactory
from website.addons.forward import utils


class TestUtils(OsfTestCase):


    def test_serialize_settings(self):
        node_settings = UbiquitypressSettingsFactory()
        serialized = utils.serialize_settings(node_settings)
        assert_equal(
            serialized,
            {
                'journal_code': node_settings.journal_code,
                'journal_settings': utils.get_journals
            }
        )


    def test_get_journals(self):
        journals = utils.get_journals()
        assert_true(journals))


