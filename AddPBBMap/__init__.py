# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AddPBBMap
                                 A QGIS plugin
 Add PBB Map from postgis database
                             -------------------
        begin                : 2016-09-07
        copyright            : (C) 2016 by Septin Mulatsih Rezki
        email                : septinmulatsihrezki@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AddPBBMap class from file AddPBBMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PBBMap import AddPBBMap
    return AddPBBMap(iface)
