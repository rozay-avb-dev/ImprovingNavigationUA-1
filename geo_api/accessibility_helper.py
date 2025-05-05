import difflib
from geo_api.accessibility_data import ACCESSIBILITY_FEATURES

# def get_accessibility_info(building_name):
#     keys = list(ACCESSIBILITY_FEATURES.keys())
#     closest = difflib.get_close_matches(building_name, keys, n=1, cutoff=0.6)
#     if closest:
#         return ACCESSIBILITY_FEATURES[closest[0]]
#     return {
#         "ramps": [],
#         "elevators": []
#     }

def get_accessibility_info(building_name):
    keys = list(ACCESSIBILITY_FEATURES.keys())
    closest = difflib.get_close_matches(building_name, keys, n=1, cutoff=0.6)
    if closest:
<<<<<<< HEAD
        print(f" Accessibility matched: {closest[0]}")
        return ACCESSIBILITY_FEATURES[closest[0]]
    print(f" Accessibility NOT found for: {building_name}")
=======
        print(f"[DEBUG] Accessibility matched: {closest[0]}")
        return ACCESSIBILITY_FEATURES[closest[0]]
    print(f"[DEBUG] Accessibility NOT found for: {building_name}")
>>>>>>> 2f8b7faf938bfb08d364521393d2be53cb89f848
    return {"ramps": [], "elevators": []}
