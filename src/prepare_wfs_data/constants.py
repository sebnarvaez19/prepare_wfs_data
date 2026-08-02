from typing import Final


COLUMNS_TO_DROP: Final[list[str]] = ["causes", "centroid", "id", "lifetime", "types"]
COLUMNS_TO_RENAME: Final[dict[str, str]] = {
    "confidence": "cluster_confidence",
    "type_string": "types",
    "cause_string": "causes",
    "area": "cluster_area",
}
COLUMNS_OBJECT: Final[list[str]] = ["algorithms", "satellites"]
COLUMNS: Final[list[str]] = [
    "oldest_acquisition",
    "newest_acquisition",
    "satellites",
    "algorithms",
    "cluster_confidence",
    "fire_confidence",
    "types",
    "causes",
    "num_fires",
    "cluster_area",
    "municipality_id",
    "geometry",
]
MUNICIPALITIES_URL: Final[str] = (
    "https://api-791856053294.us-central1.run.app/cartography/municipalities/items"
)