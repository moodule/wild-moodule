# -*- coding: utf-8 -*-

"""
=======
Ratings
=======

Augment and rate the scraped ads.
"""

from __future__ import division, print_function, absolute_import

import pprint

import googlemaps

#####################################################################
# PRINTER
#####################################################################

PP = pprint.PrettyPrinter(indent=4)

#####################################################################
# GOOGLE MAPS API
#####################################################################

KEY = "AIzaSyCDpsGLGxA8sm686Q_or5cVFQWUF_zLErs"
GMAPS_CLIENT = googlemaps.Client(key=KEY)

#####################################################################
# HOMES
#####################################################################

HOMES = [
    {"lat": 49.2128736, "lng": 5.9750234},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.4773983, "lng": 6.3147222},
    {"lat": 48.4487414, "lng": 6.7381417},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.6599676, "lng": 6.1724618},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.4245, "lng": 6.4682},
    {"lat": 48.5667028, "lng": 6.4991575},
    {"lat": 49.2583938, "lng": 5.96607933875943},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6731344, "lng": 6.1536378},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 49.2332157, "lng": 5.9669258},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.4443122, "lng": 6.7356749},
    {"lat": 48.7717193, "lng": 6.2632187},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.7717193, "lng": 6.2632187},
    {"lat": 48.9837551, "lng": 6.0197497},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.7658301, "lng": 6.1229922},
    {"lat": 48.6848709, "lng": 6.1522232},
    {"lat": 49.1569586, "lng": 5.8821708},
    {"lat": 48.5922, "lng": 6.1526},
    {"lat": 49.2302031, "lng": 6.0092074},
    {"lat": 49.3085543, "lng": 5.7846233},
    {"lat": 48.6231282, "lng": 6.3493799},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.656251, "lng": 6.2314017},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 49.2583938, "lng": 5.96607933875943},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 49.5339956, "lng": 5.8023036},
    {"lat": 48.7005548, "lng": 6.2074377},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 49.1569586, "lng": 5.8821708},
    {"lat": 48.6731344, "lng": 6.1536378},
    {"lat": 49.2249744, "lng": 5.9926232},
    {"lat": 48.9025946, "lng": 6.0547691},
    {"lat": 48.6442916, "lng": 6.4389834},
    {"lat": 48.6846355, "lng": 5.7866205},
    {"lat": 49.2583938, "lng": 5.96607933875943},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6762624, "lng": 5.8941759},
    {"lat": 49.4039, "lng": 5.844},
    {"lat": 48.6217058, "lng": 6.1609279},
    {"lat": 48.7511972, "lng": 6.1638113},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6848709, "lng": 6.1522232},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.9837551, "lng": 6.0197497},
    {"lat": 48.642538, "lng": 5.8249564},
    {"lat": 48.7053172, "lng": 6.2220764},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.466365, "lng": 6.2920365},
    {"lat": 48.6731344, "lng": 6.1536378},
    {"lat": 48.5912734, "lng": 6.8435322},
    {"lat": 48.7119046, "lng": 6.1641314},
    {"lat": 48.557112, "lng": 6.3871266},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.6256516, "lng": 6.0803932},
    {"lat": 48.7658301, "lng": 6.1229922},
    {"lat": 48.7658301, "lng": 6.1229922},
    {"lat": 49.4461066, "lng": 5.600732},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6846355, "lng": 5.7866205},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.6848709, "lng": 6.1522232},
    {"lat": 49.3901142, "lng": 5.7578871},
    {"lat": 49.1569586, "lng": 5.8821708},
    {"lat": 48.6762624, "lng": 5.8941759},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 49.2096137, "lng": 5.9352826},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 49.2128736, "lng": 5.9750234},
    {"lat": 48.7967416, "lng": 6.0996071},
    {"lat": 48.6015161, "lng": 6.4401224},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.7053172, "lng": 6.2220764},
    {"lat": 49.5107263, "lng": 5.5638451},
    {"lat": 48.6765454, "lng": 6.173258},
    {"lat": 48.7967416, "lng": 6.0996071},
    {"lat": 48.7005548, "lng": 6.2074377},
    {"lat": 48.6937223, "lng": 6.1834097},
    {"lat": 48.4632, "lng": 5.9548},
    {"lat": 48.4813289, "lng": 6.7772958},
    {"lat": 49.1968237, "lng": 5.845958},
    {"lat": 48.5916164, "lng": 6.4919563},
    {"lat": 48.6599676, "lng": 6.1724618}]

INSPE_NANCY = {"lat": 48.704244, "lng": 6.163837}
INSPE_METZ = {"lat": 49.101173, "lng": 6.150357}

#####################################################################
# FETCH DATA
#####################################################################

#####################################################################
# GEOCODE
#####################################################################

_distances_nancy = GMAPS_CLIENT.distance_matrix(HOMES, INSPE_NANCY)
_distances_metz = GMAPS_CLIENT.distance_matrix(HOMES, INSPE_METZ)

_distances = []
_durations = []
for i in range(len(HOMES)):
    _distances.append((
        _distances_nancy['rows'][i]['elements'][0]['distance']['value'] * 0.001,
        _distances_metz['rows'][i]['elements'][0]['distance']['value'] * 0.001))
    _durations.append((
        _distances_nancy['rows'][i]['elements'][0]['duration']['value'] / 60.0,
        _distances_metz['rows'][i]['elements'][0]['duration']['value'] / 60.0))

#####################################################################
# GEOCODE
#####################################################################

def geocode(
        item: dict,
        filter: dict={"country": "FR", "administrative_area_level_1": "Grand Est"}) -> dict:
    """
    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    """
    __short_serialized_location = item.get('location', '')
    __location = {}

    if __short_serialized_location:
        __probable_locations = _gmaps_client.geocode(
            __short_serialized_location,
            components=filter)
        if len(__probable_locations):
            __location['formatted_address'] = __probable_locations[0].get('formatted_address', '')
            __location['latitude'] = __probable_locations[0]['geometry']['location']['lat']
            __location['longitude'] = __probable_locations[0]['geometry']['location']['lng']
        else:
            pass # raise 'location not found in gmaps'

    else:
        pass # raise error 'location unknown'

    return __location

#####################################################################
# REAL ESTATE
#####################################################################

# garage

# price per square meter

#####################################################################
# EXPORT
#####################################################################

with open("distances.csv", "w") as _file:
    for _d in _distances:
        _file.write("{}, {}\n".format(
            round(_d[0], 1),
            round(_d[1], 1))) # (nancy, metz) in km

with open("durations.csv", "w") as _file:
    for _d in _durations:
        _file.write("{}, {}\n".format(
            round(_d[0], 0),
            round(_d[1], 0))) # in minutes
