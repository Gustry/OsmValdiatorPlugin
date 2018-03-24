
__author__ = 'Etienne Trimaille'
__date__ = '2018-02-24'
__copyright__ = '(C) 2018 by Etienne Trimaille'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsApplication

from src.osm_validator_processing.osm_validator_provider import OsmValidatorProvider


class OsmValidatorPlugin:

    def __init__(self):
        self.provider = OsmValidatorProvider()
        # noinspection PyArgumentList
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        pass

    def unload(self):
        # noinspection PyArgumentList
        QgsApplication.processingRegistry().removeProvider(self.provider)
