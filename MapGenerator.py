import folium
import random
import geoloc
import twitterAPI


def add_marker(group, coords, name, status="OK"):
    """
    (FeatureGroup, [latitude, longitude], str) -> None

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
    folium.PolyLine(locations=coord_list, weight=2).add_to(group)


def generate_map(path, acct):
    f_map = folium.Map()

    user = twitterAPI.json_get_user_info(acct)
    num = user[3]

    if user[0]:
        user_coords = geoloc.get_geo_position_ArcGIS(user[0])
        add_marker(f_map, user_coords, create_popup(user), status="POINT")
    else:
        user_coords = geoloc.random_coords()
        add_marker(f_map, user_coords, create_popup(user), status="POINT")

    friends = twitterAPI.json_get_user_friend_info(acct, num)
    x = 0
    for i in friends:
        if i[0]:
            friend_coord = geoloc.get_geo_position_ArcGIS(i[0])
            if friend_coord:
                add_marker(f_map, friend_coord, create_popup(i))
            else:
                friend_coord = geoloc.random_coords()
                add_marker(f_map, friend_coord, create_popup(i), status="NO")
        else:
            friend_coord = geoloc.random_coords()
            add_marker(f_map, friend_coord, create_popup(i), status="NO")
        add_line(f_map, [user_coords, friend_coord])

    f_map.save(path)
    return 0
