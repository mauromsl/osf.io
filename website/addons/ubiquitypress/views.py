from flask import request

from framework.auth.decorators import must_be_logged_in
from website.project.decorators import (
    must_have_addon,
    must_have_permission)

from website.addons.ubiquitypress.utils import serialize_settings, settings_complete

import requests
from pprint import pprint



@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_settings(node_addon, **kwargs):
    return serialize_settings(node_addon)


@must_have_permission('write')
@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_settings_put(auth, node_addon, **kwargs):
    """Set configuration for Ubiquitypress node settings, adding a log if URL has
    changed.

    :param-json str journal_code: Ubiquity Press journal code
    :raises: HTTPError(400) if values missing or invalid

    """
    try:
        node_addon.journal_code = request.json['journal_code']
    except (KeyError, TypeError, ValueError):
        raise HTTPError(http.BAD_REQUEST)

    # Save settings and get changed fields; crash if validation fails
    try:
        saved_fields = node_addon.save()
    except ValidationError:
        raise HTTPError(http.BAD_REQUEST)

    # Log change if URL updated
    if 'journal_code' in saved_fields:
        node_addon.owner.add_log(
            action='ubiquitypress_journal_code_changed',
            params=dict(
                node=node_addon.owner._id,
                project=node_addon.owner.parent_id,
                journal_code=node_addon.journal_code,
            ),
            auth=auth,
            save=True,
        )

    return {}


@must_have_addon('ubiquitypress', 'node')
def ubiquitypress_widget(node_addon, **kwargs):

    out = serialize_settings(node_addon)
    out['complete'] = settings_complete(node_addon)
    out.update(node_addon.config.to_json())
    print (dir(out))
    return out


