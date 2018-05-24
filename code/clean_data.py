# Takes *** seconds to run this script

print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)

if not os.path.isdir("../data/"): # Create the output directory if it doesn't exist
    os.makedirs("../data/")

print "Launching ArcGIS"
import arcpy

print "Enabling the Spatial Analyst extension"
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

print "Setting the environment"
arcpy.env.overwriteOutput = True # Allow the overwriting of the output files
arcpy.env.workspace = "../b_temp/b_temp.gdb" # Set the working directory. Some geoprocessing tools (e.g. Extract By Mask) cannot save the output unless the workspace is a geodatabase.

### Define the main function ###
def main():
  try:
    print "Inputs being set"
    arcpy.env.workspace = "../orig/"
    input_list = arcpy.ListRasters("*.DEM")

    print "Outputs being set"
    output_dir = "../data/"
    output_tif = "elevation.tif"

    print "Processing..."
    arcpy.MosaicToNewRaster_management(input_list, output_dir, output_tif, pixel_type="16_BIT_SIGNED", number_of_bands="1")
        # The number_of_bands option is required.
    	# The pixel_type option is optional, but should always be specified: the default is 8_BIT_UNSIGNED, which truncates the values greater than 255.
        # See http://desktop.arcgis.com/en/arcmap/10.4/tools/data-management-toolbox/mosaic-to-new-raster.htm for detail

    print "All geoprocessing successfully done."

  # Return geoprocessing specific errors
  except arcpy.ExecuteError:
    print arcpy.GetMessages()
  # Return any other type of error
  except:
    print "There is non-geoprocessing error."
  # Check in extensions
  finally:
    arcpy.CheckInExtension("spatial")

# subfunctions



### Execute the main function ###
if __name__ == "__main__":
    main()
