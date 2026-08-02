import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from prepare_wfs_data.spatial import load_municipalities


def plot_wildfires_clusters(gdf: gpd.GeoDataFrame, dpi: int = 150) -> tuple[Figure, Axes]:
    """

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The input GeoDataFrame containing wildfire data.
    dpi : int, optional
        The resolution of the plot, by default 150.

    Returns
    -------
    tuple[Figure, Axes]
        A tuple containing the figure and axes of the plot.
    """
    municipalities = load_municipalities().to_crs(epsg="3857")
    gdf = gdf.copy().to_crs(epsg="3857")
    gdf["cluster_confidence"] = gdf["cluster_confidence"]
    fig = plt.figure(dpi=dpi, tight_layout=True)
    ax = fig.add_subplot()
    municipalities.boundary.plot(lw=0.5, color="black", ax=ax)
    gdf.plot(column="cluster_confidence", ax=ax, legend=True, cmap="YlOrRd")
    ctx.add_basemap(ax, source=ctx.providers.OPNVKarte)
    ax.axis(False)
    return fig, ax