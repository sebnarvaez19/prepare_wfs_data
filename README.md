# Prepare WFS Data

[![PyPI Package](https://img.shields.io/badge/PyPI-prepare--wfs--data-blue?logo=pypi)](https://pypi.org/project/prepare-wfs-data/)
[![PyPI Version](https://img.shields.io/pypi/v/prepare-wfs-data)](https://pypi.org/project/prepare-wfs-data/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/sebnarvaez19/prepare_wfs_data)


Prepare data from OroraTech Wildfire Solutions to be uploaded to Risk Management API.

## Installation

To install it:
```bash
pip install prepare_wfs_data
```


## Usage

The main function is `prepare_data()` which takes a GeoDataFrame as input and returns a prepared GeoDataFrame. It receives GeoJSON data downloaded directly from OroraTech Wildfire Solutions.

```python
import pandas as pd
import geopandas as gpd
from prepare_wfs_data import prepare_data

gdf = gpd.read_file("path/to/wfs-data.geojson")
gdf = prepare_data(gdf)
```