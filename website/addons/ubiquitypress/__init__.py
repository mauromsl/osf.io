from website.addons.ubiquitypress import model, routes

import os

MODELS = [model.UbiquitypressNodeSettings]
NODE_SETTINGS_MODEL = model.UbiquitypressNodeSettings #Defines the model to enable the addon


ROUTES = [routes.api_routes]

SHORT_NAME = 'ubiquitypress'
FULL_NAME = 'Ubiquity Press'

OWNERS = ['node']

ADDED_DEFAULT = []
ADDED_MANDATORY = []

VIEWS = ['views']
CONFIGS = ['node']

CATEGORIES = ['publish']

INCLUDE_JS = {
    'page': [],
    'files': [],
}

INCLUDE_CSS = {
    'widget': [],
    'page': [],
    'files': []
}

WIDGET_HELP = 'Ubiquity Press'

HAS_HGRID_FILES = False

HERE = os.path.dirname(os.path.abspath(__file__))
NODE_SETTINGS_TEMPLATE = os.path.join(HERE, 'templates', 'ubiquitypress_node_settings.mako')
USER_SETTINGS_TEMPLATE = None  # use default user settings templates
