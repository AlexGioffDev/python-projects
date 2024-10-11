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

elev = list(volcanoes["ELEV"])


my_map = folium.Map(
    location=[48, -121.62],
    tiles="Cartodb Positron",
    zoom_start=6,
)

# Popup HTML
html = """<p style='font-weight: 300; font-style: italic;'>Volcano information:</p>
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
fg = folium.FeatureGroup(name="My Map")
# Loops Marker with Data
for lt, ln, el in zip(lat, lon, elev):
    # IFRAME
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(color=color_producer(el)),
        )
    )


my_map.add_child(fg)

my_map.save("test.html")
