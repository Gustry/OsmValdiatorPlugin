"""
/***************************************************************************
        QuickOSM QGIS plugin
        OSM Overpass API frontend
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
from os.path import join, dirname
from json import load

from processing.algs.qgis.QgisAlgorithm import QgisFeatureBasedAlgorithm
from qgis.core import (
    QgsFeatureRequest,
    QgsFileUtils,
    QgsFileDownloader,
    QgsProcessingParameterString,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterEnum,
    QgsProcessingParameterExtent,
    QgsProcessingParameterNumber,
    QgsProcessingParameterFileDestination,
    QgsProcessingOutputString,
    QgsProcessingOutputFile,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterField,
    QgsProcessingException,
    QgsProcessingAlgorithm,
    QgsCoordinateTransform,
    QgsProject,
    QgsCoordinateReferenceSystem,
    QgsFeatureSink,
    QgsVectorLayer,
)


class CheckFieldAlgorithm(QgisFeatureBasedAlgorithm):

    """Check a field according to an OSM tag."""

    # INPUT = 'INPUT'
    FIELD = 'FIELD'
    TARGET_KEY = 'TARGET_KEY'
    # OUTPUT = ' OUTPUT'

    def __init__(self):
        osm_file = join(
            dirname(dirname(dirname(dirname(__file__)))), 'mapFeatures.json')
        self.osm_features = load(open(osm_file))
        self.keys = list(self.osm_features.keys())
        super(CheckFieldAlgorithm, self).__init__()

    def group(self):
        return self.tr('Validation')

    def groupId(self):
        return 'validation'

    @staticmethod
    def name():
        return 'osm_check_field'

    def displayName(self):
        return self.tr('Check OSM key')

    def outputName(self):
        return self.tr('errors')

    def initParameters(self, config=None):
        self.addParameter(QgsProcessingParameterField(
            self.COLUMNS,
            self.tr('Field to check'),
            None,
            'INPUT',
            QgsProcessingParameterField.Any,
            True))

        self.addParameter(QgsProcessingParameterEnum(
            self.TARGET_KEY,
            self.tr('Key'),
            options=self.keys
        ))

    def initAlgorithm(self, config=None):
        # self.addParameter(QgsProcessingParameterFeatureSource(
        #     self.VECTOR_LAYER,
        #     self.tr('Vector layer')
        # ))

        # self.addParameter(QgsProcessingParameterField(
        #     self.FIELD,
        #     self.tr('Field'),
        #     parentLayerParameterName=self.INPUT
        # ))


        #
        # self.addParameter(QgsProcessingParameterFeatureSink(
        #     self.OUTPUT,
        #                                                     self.tr('Converted')))
        # super(CheckFieldAlgorithm, self).initAlgorithm()
        pass

    def outputFields(self, input_fields):
        # loop through twice - first we need to build up a list of original attribute indices
        for f in self.fields_to_delete:
            index = input_fields.lookupField(f)
            self.field_indices.append(index)

        # important - make sure we remove from the end so we aren't changing used indices as we go
        self.field_indices.sort(reverse=True)

        # this second time we make a cleaned version of the fields
        for index in self.field_indices:
            input_fields.remove(index)
        return input_fields

    def prepareAlgorithm(self, parameters, context, feedback):
        self.field = self.parameterAsFields(parameters, self.FIELD, context)
        self.key = self.parameterAsEnum(parameters, self.TARGET_KEY, context)
        # layer = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        # self.index = layer.fieldNameIndex(self.keys[self.key])
        return True

        # self.expression_context.setFeature(feature)
        #
        #
        # value = self.expression.evaluate(self.expression_context)
        # if self.expression.hasEvalError():
        #     raise QgsProcessingException(
        #         self.tr('Evaluation error: {0}').format(self.expression.evalErrorString()))
        #
        # if not value:
        #     feature.setGeometry(QgsGeometry())
        # else:
        #     if not isinstance(value, QgsGeometry):
        #         raise QgsProcessingException(
        #             self.tr('{} is not a geometry').format(value))
        #     feature.setGeometry(value)
        # return [feature]

    def processFeature(self, feature, context, feedback):
        print(self.)

