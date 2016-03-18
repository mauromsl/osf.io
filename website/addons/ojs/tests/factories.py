"""Factory boy factories for the ubiquitypress addon."""

from factory import SubFactory
from tests.factories import ModularOdmFactory, ProjectFactory

from website.addons.ubiquitypress.model import UbiquitypressNodeSettings


class UbiquitypressSettingsFactory(ModularOdmFactory):

    FACTORY_FOR = UbiquitypressNodeSettings

    owner = SubFactory(ProjectFactory)
    journal_code = 'cg'
