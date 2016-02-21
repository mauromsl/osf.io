from flask import request

from framework.auth.decorators import must_be_logged_in
from website.project.decorators import must_have_addon

from website.addons.ubiquitypress.utils import serialize_settings

import requests



@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_settings(node_addon, **kwargs):
    print ('UBIQUITY PRESS CONFIG')
    return serialize_settings(node_addon)


@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_widget(**kwargs):

    journals_api = requests.get('http://jura.ubiquity.press/api/public/journals/')
    journals = journals_api.json()

    return {'journals':journals}


