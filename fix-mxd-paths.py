import arcpy
import datetime
import os
import string
import sys

oldDataPath = arcpy.GetParameterAsText(0)
newGeoDB = arcpy.GetParameterAsText(1)
mxd = arcpy.mapping.MapDocument("CURRENT")


mxd.findAndReplaceWorkspacePaths("", str(newGeoDB), False)

mxd.save
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
elementsArray = ["DATAFRAME_ELEMENT", "GRAPHIC_ELEMENT", "MAPSURROUND_ELEMENT", "PICTURE_ELEMENT", "TEXT_ELEMENT"]

for index in range(len(elementsArray)):
    arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    msg = arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    arcpy.AddMessage("Map Element: "+str(msg))
mxd.save()
