import geopandas as gpd
import pandas as pd
import requests

from prepare_wfs_data.constants import MUNICIPALITIES_URL


def load_municipalities() -> gpd.GeoDataFrame:
    """
    Load municipalities from the WFS service and return a GeoDataFrame.

    Returns
    -------
    gpd.GeoDataFrame
        A GeoDataFrame containing municipality data with columns ["id", "name", "geometry"].
    """
    response = requests.get(MUNICIPALITIES_URL)
    if response.status_code != 200:
        raise Exception(response.content)
    df = pd.DataFrame.from_records(response.json())
    geometry = gpd.GeoSeries.from_wkt(df["geometry"], crs="EPSG:9377")
    gdf = gpd.GeoDataFrame(df[["id", "name"]], geometry=geometry).set_index("id")
    return gdf


def intersect_municipalities(gdf: gpd.GeoDataFrame, crs: str = "EPSG:9377") -> gpd.GeoDataFrame:
    """
    Intersect the input GeoDataFrame with municipalities.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame.
    crs : str, optional
        The Coordinate Reference System to use, by default "EPSG:9377".

    Returns
    -------
    gpd.GeoDataFrame
        The GeoDataFrame with municipality information added.
    """
    gdf = gdf.copy().to_crs(crs)
    municipalities = load_municipalities().to_crs(crs)
    municipalities.index.name = "municipality_id"
    municipalities = municipalities.drop(columns=["name"])
    geometry = gdf.geometry.copy()
    gdf.geometry = gdf.geometry.centroid
    result = gdf.sjoin(municipalities, how="inner", predicate="intersects")
    result.geometry = geometry
    return result