from flask import request

from framework.auth.decorators import must_be_logged_in

from website.project.decorators import (
    must_be_contributor_or_public,
    must_have_permission,
    must_not_be_registration,
    must_have_addon,
)

import requests
import serializer



@must_have_addon('ubiquitypress', 'node_addon')
def up_settings(auth):

    return {'result': 'test'}


@must_have_addon('ubiquitypress', 'node_addon')
def up_get_journals(auth):

    journals_api = requests.get('http://jura.ubiquity.press/api/public/journals/')
    journals = journals_api.json()

    return {'journals':journals}


@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_widget(node_addon, **kwargs):


    journals_api = requests.get('http://jura.ubiquity.press/api/public/journals/')
    journals = journals_api.json()

    return {'journals':journals}




