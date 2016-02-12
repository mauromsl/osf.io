from website.addons.base import AddonOAuthNodeSettingsBase
from website.addons.base import AddonOAuthUserSettingsBase
from website.addons.citations.utils import serialize_folder
from website.addons.ubiquitypress import serializer
from website.addons.ubiquitypress import settings
from website.oauth.models import ExternalProvider
from website.util import web_url_for
from website.addons.base import AddonNodeSettingsBase

class UbiquitypressNodeSettings(AddonNodeSettingsBase):

    complete = True

    journal = None
    
    @property
    def link_text(self):
        return self.label if self.label else self.url

    def on_delete(self):
        self.reset()

    def reset(self):
        self.url = None
