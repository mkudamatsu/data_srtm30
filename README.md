This repository downloads and clean SRTM30 (elevation raster data) for its use in ArcGIS 10.

Currently, the tiles `e020n90` and `e020n40` are downloaded (see [WebGIS's page](http://www.webgis.com/srtm30.html) for where these tiles are).

But the user can change the line 21 in `download_data.py` to download other tiles.

Then `clean_data.py` uses ArcGIS 10 to append multiple tiles into one TIFF raster as `data/elevation.tif`.
