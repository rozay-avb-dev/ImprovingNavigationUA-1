import difflib
from geo_api.accessibility_data import ACCESSIBILITY_FEATURES

def get_accessibility_info(building_name):
    keys = list(ACCESSIBILITY_FEATURES.keys())
    closest = difflib.get_close_matches(building_name, keys, n=1, cutoff=0.6)
    if closest:
        return ACCESSIBILITY_FEATURES[closest[0]]
    return {
        "ramps": [],
        "elevators": []
    }
