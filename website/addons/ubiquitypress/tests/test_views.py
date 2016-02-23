from nose.tools import *

from website.addons.ubiquityoress.tests.utils import UbiquitypressAddonTestCase


class TestForwardLogs(ForwardAddonTestCase):

    def setUp(self):
        super(TestForwardLogs, self).setUp()
        self.app.authenticate(*self.user.auth)

    def test_change_journal_log_added(self):
        log_count = len(self.project.logs)
        self.app.put_json(
            self.project.api_url_for('ubiquitypress_settings_put'),
            dict(
                url='sta',
            ),
        )
        self.project.reload()
        assert_equal(
            len(self.project.logs),
            log_count + 1
        )

