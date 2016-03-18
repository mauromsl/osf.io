from framework.routing import Rule, json_renderer
from website.routes import OsfWebRenderer

from website.addons.ojs import views

api_routes = {

    'rules': [

        Rule(
            [
                '/project/<pid>/ojs/config/',
                '/project/<pid>/node/<nid>/ojs/config/'
            ],
            'get',
            views.ojs_settings,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/ojs/config/',
                '/project/<pid>/node/<nid>/ojs/config/'
            ],
            'put',
            views.ojs_settings_put,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/ojs/widget/',
                '/project/<pid>/node/<nid>/ojs/widget/',
            ],
            'get',
            views.ojs_widget,
            OsfWebRenderer('../addons/ojs/templates/ojs_widget.mako'),
        )

    ],


    'prefix': '/api/v1',

}
