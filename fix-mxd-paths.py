import arcpy
import os

oldDataPath = arcpy.GetParameterAsText(0)
newGeoDB = arcpy.GetParameterAsText(1)

mxd = arcpy.mapping.MapDocument("CURRENT")

