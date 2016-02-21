from website.addons.base import AddonNodeSettingsBase
from modularodm import fields

class UbiquitypressNodeSettings(AddonNodeSettingsBase):

    journal_code = fields.StringField()


    def on_delete(self):
        self.reset()

    def reset(self):
        self.journal_code = None

    def api_endpoint(self):
    	return utils.get_journal_url(self.journal_code)




