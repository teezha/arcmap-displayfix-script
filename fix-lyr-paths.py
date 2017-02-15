import arcpy
import os

lyrPath = arcpy.GetParameterAsText(0)

mxd = arcpy.mapping.MapDocument("CURRENT")

homeFrame = mxd.activeDataFrame
for data in homeFrame:
	if data.name == "Layers":
		thisFrame = data
		lExt = thisFrame.getExtent()
		fExt = homeFrame.extent
		fExt = lExt
		thisFrame.extent = fExt

arcpy.RefreshActiveView()

elementsArray = ["DATAFRAME_ELEMENT", "GRAPHIC_ELEMENT", "MAPSURROUND_ELEMENT", "PICTURE_ELEMENT", "TEXT_ELEMENT"]

for index in range(len(elementsArray)):
    arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    msg= arcpy.mapping.ListLayoutElements(mxd,elementsArray[index])
    arcpy.AddMessage("Map Element: "+str(msg))

mxd.save()
