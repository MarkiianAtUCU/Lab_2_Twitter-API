import folium
import random
import geoloc
import twitterAPI


def add_marker(group, coords, name, status="OK"):
    """
    (FeatureGroup, [latitude, longitude], status="OK") -> None
                                                  "POINT"
                                                  "NO"

    Function adds folium marker to folium.FeatureGroup() or folium.Map()
    """
    if status == "OK":
        icon = folium.Icon(color='green', icon='ok-circle')
    elif status == "POINT":
        icon = folium.Icon(color='orange', icon='record')
    else:
        icon = folium.Icon(color='red', icon='remove-circle')

    folium.Marker(location=coords, popup=name, icon=icon).add_to(group)


def create_popup(js):
    """
    (dict) -> str
    Function returns info from json dictionary in formatted html tags view
    """
    res = """<img src="{}"/><br>
    Name: {}<br>
    Location: {}<br>
    Lang: {}<br>
    Friends: {}<br>
    Followers: {}<br>
    Created at: {}<br>
    """.format(js[1], js[2], js[0], js[6], js[3], js[4], js[5])
    return res.replace("'", "`")


def add_line(group, coord_list):
    """
    (FeatureGroup, ([latitude, longitude], [latitude, longitude])

    Function adds folium line to folium.FeatureGroup() or folium.Map()
    """
    folium.PolyLine(locations=coord_list, weight=2).add_to(group)


def create_user_marker(acct):
    """
    (str) -> (int, [latitude, longitude], str)

    Function returns location, friends number and info about twitter user
    """
    user = twitterAPI.json_get_user_info(acct)
    friend_num = user[3]
    if user[0]:
        user_coords = geoloc.get_geo_position_ArcGIS(user[0])
        if not user_coords:
            user_coords = geoloc.random_coords()
    else:
        user_coords = geoloc.random_coords()
    return friend_num, user_coords, create_popup(user)


def create_friend_marker(js):
    """
    (str) -> (int, [latitude, longitude], str)

    Function returns location, friends number and info about twitter user
    and type of marker:
                        "OK" - found location
                        "NO" - did not find location
    """
    status = "OK"
    if js[0]:
        friend_coord = geoloc.get_geo_position_ArcGIS(js[0])
        if not friend_coord:
            status = "NO"
            friend_coords = geoloc.random_coords()
    else:
        status = "NO"
        friend_coord = geoloc.random_coords()
    return friend_coord, create_popup(js), status
