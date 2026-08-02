import geopandas as gpd
import matplotlib.pyplot as plt
from prepare_wfs_data import prepare_data
from prepare_wfs_data.plot import plot_wildfires_clusters


if __name__ == "__main__":
    gdf = gpd.read_file("data/wfs-area-export-Atlantico_2026-01-01-2026-08-02.geojson")
    gdf = prepare_data(gdf)
    print(gdf.info())
    plot_wildfires_clusters(gdf)
    plt.show()
