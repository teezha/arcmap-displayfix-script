import arcpy
import os

oldDataPath = arcpy.GetParameterAsText(0)
newGeoDB = arcpy.GetParameterAsText(1)

mxd = arcpy.mapping.MapDocument("CURRENT")
mxd.findAndReplaceWorkspacePaths(oldDataPath, newGeoDB)

arcpy.RefreshTOC()
arcpy.RefreshActiveView()

elementsArray = ["DATAFRAME_ELEMENT", "GRAPHIC_ELEMENT", "MAPSURROUND_ELEMENT", "PICTURE_ELEMENT", "TEXT_ELEMENT"]

for index in range(len(elementsArray)):
    arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    msg= arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    arcpy.AddMessage("Map Element: "+msg)

mxd.save()
