# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# mod5.py
# Created on: 2017-02-13 14:25:09.00000
# Made by Toby Zhang A00987765
# Description: This script find existing layers the user wishes to delete and add new layers from user input 
# The script then prints out a PDF of the Crime_Intents data frame and a jpeg image of the entire layout
# 1) Takes input feature classes the user wishes to delete and/or add
# 2) Checks for feature class layer, then deletes each instance if present
# 3) Adds the user chosen layer to the map document
# 4) Prints out a pdf of the Crime_Intents layer
# 5) Prints out a jpeg of the entire layout
# Dependencies: Crime_Intents must be an available data frame in order for the pdf to print out. Other values are optional to exist for hte script to work
#============================================================================ 

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
	# List all data frames controlled by selector string at the end. This returns a list even if only one is selected thus index is at 0 for the array
	findFrame = arcpy.mapping.ListDataFrames(mxd, "Crime")[0]
	allFrame = arcpy.mapping.ListDataFrames(mxd)
	# Creates a Layer object from path
	addLyr = arcpy.mapping.Layer(str(addDataPath))
	# Finds the data frame -> adds the layer -> allow the new layer to be grouped with similair feature classes
	arcpy.mapping.AddLayer(findFrame, addLyr, "AUTO_ARRANGE")

	# splits path from user input
	drive, pathnfile = os.path.splitdrive(deleteDataPath)
	path, file = os.path.split(pathnfile)
	
	# for each data frome from all frames available...
	for delFram in allFrame:
		# Prints out each frame's name as the for loop progresses
		arcpy.AddMessage(delFram.name)
		# for each layer in each data frame...
		for thislyr in arcpy.mapping.ListLayers(mxd, "",delFram):
			# If a layer matches the file name, file path, or layer name...
			if (thislyr.dataSource == deleteDataPath)|(delFram.name == file)|(delFram.name == "Bexar_Countr_Boundary"):
				# Gives the user the name of the layer then deletes the layer		
				arcpy.AddMessage(thislyr.name)
				arcpy.mapping.RemoveLayer(delFram, thislyr)
	
	# List the data frame that is called Crime_Inset
	crimeInsetFrame = arcpy.mapping.ListDataFrames(mxd, "Crime_Inset")[0]
	
	# Splits path from user input, creates output path
	drive, pathnfile = os.path.splitdrive(addDataPath)
	path, file = os.path.split(pathnfile)
	filepath = drive +"\\" + path +"\\"  
	# Tells user what the output path is
	arcpy.AddMessage(filepath)
	# Creates a pdf and jpeg from user input. PDF has control variable of only printing the Crime_Inset.
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
