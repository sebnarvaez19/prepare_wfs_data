
import geopandas as gpd

from prepare_wfs_data.spatial import intersect_municipalities
from prepare_wfs_data.table import (
    drop_unnecessary_columns,
    object_to_string_columns,
    rename_columns,
    sort_columns,
)   


def prepare_data(gdf: gpd.GeoDataFrame, crs: str = "EPSG:9377") -> gpd.GeoDataFrame:
    """
    Prepare wildfire data by cleaning, renaming columns, converting objects to strings, 
    intersecting with municipalities, and sorting columns.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame containing wildfire data.
    crs : str, optional
        The Coordinate Reference System to use, by default "EPSG:9377".

    Returns
    -------
    gpd.GeoDataFrame
        The prepared GeoDataFrame.
    """
    gdf = drop_unnecessary_columns(gdf)
    gdf = rename_columns(gdf)
    gdf = object_to_string_columns(gdf)
    gdf = intersect_municipalities(gdf, crs)
    gdf = sort_columns(gdf)
    return gdf
