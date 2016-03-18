import settings

def serialize_settings(node_addon):
    return {
        'journal_url': node_addon.journal_url,
    }

def settings_complete(node_addon):
    return (
        node_addon.journal_url is not None
    )
