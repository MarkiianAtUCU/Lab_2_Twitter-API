import folium
import random
import geoloc
import twitterAPI


def add_marker(group, coords, name):
    """
    (FeatureGroup, [latitude, longitude], str) -> None

    Function adds folium marker to folium.FeatureGroup() or folium.Map()
    """
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
                  'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
                  'darkpurple', 'pink', 'lightblue', 'lightgreen',
                  'gray', 'black', 'lightgray']
    folium.Marker(
        location=coords,
        popup=name,
        icon=folium.Icon(color=random.choice(color_list), icon='film')
    ).add_to(group)


def create_popup(js):
    res = """<img src="{}"/>\n
    Name: {}\n
    Location: {}\n
    Lang: {}\n
    Friends: {}\n
    Followers: {}\n
    Created at: {}\n
    """.format(js[1], js[2], js[0], js[6], js[3], js[4], js[5])
    return res


def generate_map(path, acct):
    f_map = folium.Map()
    user = twitterAPI.json_get_user_info(acct)
    num = user[3]
    if user[0]:
        add_marker(f_map, geoloc.get_geo_position_ArcGIS(
            user[0]), create_popup(user))
    else:
        add_marker(f_map, [0, 0], user[2])

    friends = twitterAPI.json_get_user_friend_info(acct, num)
    for i in friends:
        if i[0]:
            add_marker(f_map, geoloc.get_geo_position_ArcGIS(
                i[0]), create_popup(i))

    f_map.save(path)


generate_map("Lul.html", "elonmusk")
