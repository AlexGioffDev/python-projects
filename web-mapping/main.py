"""
Author: Alex Gioffre'
Email: alex.gioffre_dev@outlook.it
GitHub: https://github.com/AlexGioffDev
"""

import folium
import pandas


# Read Data from Volcanoes.txt
volcanoes = pandas.read_csv("data/Volcanoes.txt")

# Convert Column to a list
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
name = list(volcanoes['NAME'])
elev = list(volcanoes["ELEV"])


my_map = folium.Map(
    location=[48, -121.62],
    tiles="Cartodb Positron",
    zoom_start=6,
)

# Popup HTML
html = """<p style='font-weight: 300; font-style: italic;'>%s information:</p>
<ul>
  <li style='color: green'>Height: %s m</li>
</ul>
"""


# Functions Colors
def color_producer(elevation: float) -> str:
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"

    return "red"


# Add Marker
fgv = folium.FeatureGroup(name="Volcanoes")
# Loops Marker with Data
for lt, ln, el, nm in zip(lat, lon, elev, name):
    # IFRAME
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe),
                            fill_color=color_producer(el), color= "black", fill_opacity=0.7)
    )

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=(open('data/world.json', 'r', encoding='utf-8-sig').read()),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))


my_map.add_child(fgv)
my_map.add_child(fgp)
my_map.add_child(folium.LayerControl())


my_map.save("test.html")
