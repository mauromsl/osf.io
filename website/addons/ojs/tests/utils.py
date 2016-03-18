from webtest_plus import TestApp

import website
from website.addons.base.testing import AddonTestCase


class UbiquitypressAddonTestCase(AddonTestCase):

    ADDON_SHORT_NAME = 'ubiquitypress'

    OWNERS = ['node']
    NODE_USER_FIELD = None

    def set_user_settings(self, settings):
        pass

    def set_node_settings(self, settings):
        settings.journal_code = 'cg'