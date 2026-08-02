import geopandas as gpd
import matplotlib.pyplot as plt
from prepare_wfs_data import prepare_data
from prepare_wfs_data.plot import plot_wildfires_clusters


if __name__ == "__main__":
    gdf_1 = gpd.read_file("data/wfs-area-export-Atlantico_2026-01-01-2026-08-02.geojson")
    gdf_2 = prepare_data(gdf_1)
    assert len(gdf_1.geometry) >= len(gdf_2.geometry)
    plot_wildfires_clusters(gdf_2)
    plt.show()
