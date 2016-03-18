from website.addons.ojs import model, routes

import os

MODELS = [model.OjsNodeSettings]
NODE_SETTINGS_MODEL = model.OjsNodeSettings #Defines the model to enable the addon


ROUTES = [routes.api_routes]

SHORT_NAME = 'ojs'
FULL_NAME = 'OJS'

OWNERS = ['node']

ADDED_DEFAULT = []
ADDED_MANDATORY = []

VIEWS = ['widget']
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

WIDGET_HELP = 'OJS'

HAS_HGRID_FILES = False

HERE = os.path.dirname(os.path.abspath(__file__))
NODE_SETTINGS_TEMPLATE = os.path.join(HERE, 'templates', 'ojs_node_settings.mako')
USER_SETTINGS_TEMPLATE = None  # use default user settings templates
