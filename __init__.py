
__author__ = 'Etienne Trimaille'
__date__ = '2018-02-24'
__copyright__ = '(C) 2018 by Etienne Trimaille'


import inspect
import os
import sys

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OSM Validator plugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .osm_validator import OsmValidatorPlugin
    return OsmValidatorPlugin()
