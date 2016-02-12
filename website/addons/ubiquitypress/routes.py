from framework.routing import Rule, json_renderer
from website.routes import OsfWebRenderer

from website.addons.ubiquitypress import views

api_routes = {

    'rules': [

        Rule(
            [
                '/project/<pid>/ubiquitypress/config/',
                '/project/<pid>/node/<nid>/ubiquitypress/config/'
            ],
            'get',
            views.up_settings,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/ubiquitypress/config/',
                '/project/<pid>/node/<nid>/ubiquitypress/config/'
            ],
            'put',
            views.up_get_journals,
            json_renderer,
        ),
        Rule(
            [
                '/project/<pid>/ubiquitypress/widget/',
                '/project/<pid>/node/<nid>/ubiquitypress/widget/',
            ],
            'get',
            views.ubiquitypress_widget,
            OsfWebRenderer('../addons/ubiquitypress/templates/ubiquitypress_widget.mako'),
        )

    ],

}
