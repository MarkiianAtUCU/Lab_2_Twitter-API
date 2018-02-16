import folium
import random
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

def generate_map(path):
	f_map = folium.Map()
	add_marker(f_map, [12,12], "Lul")
	f_map.save(path)
	