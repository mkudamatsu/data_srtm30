This repository downloads and cleans SRTM30 (elevation raster data; see [Farr et al. (2007)](http://doi.org/10.1029/2005RG000183) for detail) for its use in ArcGIS 10.

Currently, the tiles `e020n90` and `e020n40` are downloaded (see [WebGIS's page](http://www.webgis.com/srtm30.html) for where these tiles are).

But the user can change the line 21 in `download_data.py` to download other tiles.

Then `clean_data.py` uses ArcGIS 10 to append multiple tiles into one TIFF raster as `data/elevation.tif`.

In addition, `calculate_ruggedness.py` creates a TIFF raster `data/ruggedness.tif` of Terrain Ruggedness Index, proposed by [Riley et al. (1999)](https://download.osgeo.org/qgis/doc/reference-docs/Terrain_Ruggedness_Index.pdf). This index is known to predict GDP per capita ([Nunn and Puga 2012](http://doi.org/10.1162/REST_a_00161) and nighttime light ([Henderson et al. 2018](http://doi.org/10.1093/qje/qjx030)) across the world. Thus, it is a standard practive among ecoomists to include this variable as a regressor in the regression analysis of any kind on economic activities.
