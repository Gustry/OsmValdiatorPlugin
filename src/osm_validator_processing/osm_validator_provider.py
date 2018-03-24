# -*- coding: utf-8 -*-

"""
/***************************************************************************
 QuickOSM
                                 A QGIS plugin
 Download OpenStreetMap data
                              -------------------
        begin                : 2017-11-11
        copyright            : (C) 2017 by Etienne Trimaille
        email                : etienne dot trimaille at gmail dot com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Etienne Trimaille'
__date__ = '2017-11-11'
__copyright__ = '(C) 2017 by Etienne Trimaille'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingProvider

from OSMValidator.src.osm_validator_processing.field_validator.check_field import CheckFieldAlgorithm
from OSMValidator.src.utilities.utilities import resources_path


class OsmValidatorProvider(QgsProcessingProvider):

    def id(self, *args, **kwargs):
        return 'osmvalidator'

    def name(self, *args, **kwargs):
        return 'OSM Validator'

    def icon(self):
        return QIcon(resources_path('osm-validator.png'))

    # def svgIconPath(self):
    #     return resources_path('QuickOSM.svg')

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(CheckFieldAlgorithm())

    def supportsNonFileBasedOutput(self):
        return True

