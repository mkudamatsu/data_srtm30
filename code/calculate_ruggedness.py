# Takes 114 seconds to run this script

print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)

print "Launching ArcGIS"
import arcpy

print "Enabling the Spatial Analyst extension"
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

print "Setting the environment"
arcpy.env.overwriteOutput = True # Allow the overwriting of the output files

if not os.path.isdir("../temp/"): # Create the temporary file directory if it doesn't exist
    os.makedirs("../temp/")
arcpy.env.workspace = "../temp/" # Set the working directory. Some geoprocessing tools (e.g. Extract By Mask) cannot save the output unless the workspace is a geodatabase.

### Define the main function ###
def main():
  try:
    print "Inputs being set"
    input_tif = "../data/elevation.tif"

    print "Outputs being set"
    output_tif = "../data/ruggedness.tif"

    print "Processing..."
    get_ruggedness_index(input_tif, output_tif)

    print "Deleting the temporary file directory"
    tempdir = "../temp/"
    for file in os.listdir(tempdir):
        print file
        os.remove(tempdir+file)
    os.rmdir(tempdir)

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
def get_ruggedness_index(input_raster, output_raster):
    print "... Reading the input elevation data as a floating value Raster Object"
    elev = Float(input_raster)
      # SRTM30 is an integer raster (Integer raster cells cannot have values larger than 2,147,483,647 and thus should be avoided anyway).
      # The Raster() method would read the data as an integer raster.
      # When we square it, the output raster object becomes a floating value raster.
      # Mixing integer and float raster objects in arithmetics seems to cause an error for some reason.

    print "... Calculating the sum of elevation in the surrounding 3x3 cells"
    sum_elev = FocalStatistics(elev, statistics_type="SUM")

    print "... Calculating elevation squared"
    elev_sq = elev**2 # This would turn the output into a floating value raster, if we read the data as an integer raster object.

    print "... Calculating the sum of elevation squared in the surrounding 3x3 cells"
    sum_elev_sq = FocalStatistics(elev_sq, statistics_type="SUM")

    print "... Calculating the index"
    # The direct calculation
    #    tri_square = sum_elev_sq - 2*elev*sum_elev + 9*elev_sq
    # does not work for some reason.
    # So we break it down.
    print "... (1) Calculating the 2nd term for the index squared"
    tri_2nd = 2*elev*sum_elev
    print "... (2) Calculating the 3rd term for the index squared"
    tri_3rd = 9*elev_sq
    print "... (3) Calculating the index squared step 1"
    tri_square1 = sum_elev_sq + tri_3rd
    print "... (4) Calculating the index squared step 2"
    tri_square2 = tri_square1 - tri_2nd
    print "... (5) Calculating the index"
    tri = SquareRoot(tri_square2)

    print "... Saving the output raster"
    tri.save(output_raster)

### Execute the main function ###
if __name__ == "__main__":
    main()

### Release the memory ###
del arcpy
