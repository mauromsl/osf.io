from website.addons.base import AddonNodeSettingsBase
from modularodm import fields
from modularodm.validators import URLValidator

class OjsNodeSettings(AddonNodeSettingsBase):

    journal_url = fields.StringField(validate=URLValidator())


    def on_delete(self):
        self.reset()

    def reset(self):
        self.journal_code = None

    def api_endpoint(self):
    	return utils.get_journal_url(self.journal_code)




