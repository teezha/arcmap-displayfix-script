# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# mod5.py
# Created on: 2017-02-13 14:25:09.00000
# Made by Toby Zhang A00987765
# Description: This script find existing paths ass to generate a point feature class with the csv file
# This file does the following steps in order:
# 1) Takes input CSV file and reference for spatial reference
# 2) Checks if pre-existing file is present, then deletes it if present
# 3) Adds a ParValue, Lat and Long field and sets the data type
# 4) Fills in the table with the CSV data and creating a point for each row of data
# Dependencies: The csv data must be about partiticulate data with the particulate value, lat, and long in the exact order for this script to work.
# The csv data must also be seperated with commas and not anything else. The csv file must also contain numeric data only.
# ---------------------------------------------------------------------------

# Import modules
import arcpy
import datetime
import os
import string
import sys
import re
try:
	# Create text paths
	addDataPath = arcpy.GetParameterAsText(0)
	deleteDataPath = arcpy.GetParameterAsText(1)

	# Sets the variable for the map document (.mxd)
	mxd = arcpy.mapping.MapDocument("CURRENT")

	findFrame = arcpy.mapping.ListDataFrames(mxd, "Crime")[0]
	allFrame = arcpy.mapping.ListDataFrames(mxd)
	addLyr = arcpy.mapping.Layer(str(addDataPath))
	arcpy.mapping.AddLayer(findFrame, addLyr, "AUTO_ARRANGE")

	drive, pathnfile = os.path.splitdrive(deleteDataPath)
	path, file = os.path.split(pathnfile)
	for delFram in allFrame:
		arcpy.AddMessage(delFram.name)
		for thislyr in arcpy.mapping.ListLayers(mxd, "",delFram):
			if (thislyr.dataSource == deleteDataPath)|(delFram.name == file)|(delFram.name == "Bexar_Countr_Boundary"):
						
				arcpy.AddMessage(thislyr.name)
				arcpy.mapping.RemoveLayer(delFram, thislyr)

	crimeInsetFrame = arcpy.mapping.ListDataFrames(mxd, "Crime_Inset")[0]
	drive, pathnfile = os.path.splitdrive(addDataPath)
	path, file = os.path.split(pathnfile)
	filepath = drive +"\\" + path +"\\"  
	arcpy.AddMessage(filepath)
	arcpy.mapping.ExportToPDF(mxd, filepath+"\\Crime_Inset.pdf", crimeInsetFrame)
	arcpy.mapping.ExportToJPEG(mxd, filepath+"\\allmap.jpeg, ", "PAGE_LAYOUT")
	
# arcpy error
except arcpy.ExecuteError:
	arcpy.AddError("Arcpy related error")
	traceback.print_stack()
	traceback.print_exc()
# global execute error
except:
	arcpy.AddError("Global execute error")
	traceback.print_stack()
	traceback.print_exc()
