import requests
import os
import settings

def get_journal_url(journal_code):

	journal_endpoint = os.path.join(settings.JOURNALS_API,journal_code)
	jura_request = requests.get(journal_endpoint)
	journal_details = jura_request.json()
	journal_url = journal_details.get('live_url')

	return os.path.join(journal_url, settings.OSF_PATH)

def get_journals():
	api_request = requests.get(settings.JOURNALS_API)
	return api_request.json()

def serialize_settings(node_addon):
    return {
        'journal_code': node_addon.journal_code,
        'journals': get_journals(),
    }

def settings_complete(node_addon):
    return (
        node_addon.journal_code is not None
    )
