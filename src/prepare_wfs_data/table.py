import geopandas as gpd
import pandas as pd

from prepare_wfs_data.constants import (
    COLUMNS,
    COLUMNS_OBJECT,
    COLUMNS_TO_DROP,
    COLUMNS_TO_RENAME,
)


def object_to_string_column(s: pd.Series) -> pd.Series:
    """
    Convert a pandas Series of objects (e.g., lists) to a Series of comma-separated strings.

    Parameters
    ----------
    s : pd.Series
        The input pandas Series containing list-like objects.

    Returns
    -------
    pd.Series
        A pandas Series where each element is a comma-separated string.
    """
    return s.map(lambda x: ",".join(x))


def drop_unnecessary_columns(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Drop predefined unnecessary columns from a GeoDataFrame.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame from which columns will be dropped.

    Returns
    -------
    gpd.GeoDataFrame
        A new GeoDataFrame with the specified columns removed.
    """
    gdf = gdf.copy()
    return gdf.drop(columns=COLUMNS_TO_DROP)


def rename_columns(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Rename predefined columns in a GeoDataFrame based on a mapping.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame whose columns will be renamed.

    Returns
    -------
    gpd.GeoDataFrame
        A new GeoDataFrame with the columns renamed.
    """
    gdf = gdf.copy()
    return gdf.rename(columns=COLUMNS_TO_RENAME)


def sort_columns(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Reorder the columns of a GeoDataFrame based on a predefined list.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame to be reordered.

    Returns
    -------
    gpd.GeoDataFrame
        A new GeoDataFrame with columns sorted according to the predefined order.
    """
    gdf = gdf.copy()
    return gdf[COLUMNS]
    

def object_to_string_columns(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Convert specific predefined columns containing objects into comma-separated strings.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame containing object columns to be converted.

    Returns
    -------
    gpd.GeoDataFrame
        A new GeoDataFrame with the specified object columns converted to strings.
    """
    gdf = gdf.copy()
    for c in COLUMNS_OBJECT:
        gdf[c] = object_to_string_column(gdf[c])
    return gdf