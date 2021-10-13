import folium
import numpy as np
import pandas as pd

municipios = pd.read_csv(
    "S:\gits_stella\Python\MATOPIBA_economia_regional\matopiba_economia_regional\MATOPIBA_economia_regional\dados\exportacao_municipio_long_lag.csv")

map = folium.Map(location=[-10.349758, -45.099599],  zoom_start=5.7,
                 tiles='Stamen Terrain')

for index, linha in municipios.iterrows():
    folium.Marker([linha["LAT"], linha['LONG']], popup=linha["MUNICIPIO"],
                  icon=folium.Icon(color='green', icon_color='#003300',
                  icon='money',
                  prefix='fa')).add_to(map)

# Localização portos


suape = folium.Marker(location=[-8.394300, -34.974042],
                      popup='Porto de Suape',
                      tooltip='Porto de Suape',
                      icon=folium.Icon(color='pink',
                                             icon='ship',
                                             prefix='fa')
                      ).add_to(map)

itaqui = folium.Marker(location=[-2.5776877, -44.3725798],
                       popup='Porto de Itaqui',
                       tooltip='Porto de Itaqui',
                       icon=folium.Icon(color='blue',
                                              icon='ship',
                                              prefix='fa')
                       ).add_to(map)

pecem = folium.Marker(location=[-3.549508, -38.810846],
                      popup='Porto de Pécem',
                      tooltip='Porto de Pécem',
                      icon=folium.Icon(color='red',
                                             icon='ship',
                                             prefix='fa')
                      ).add_to(map)

# gerenciar tiles

folium.raster_layers.TileLayer(
    tiles="http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attr="google",
    name="google maps",
    max_zoom=20,
    subdomains=["mt0", "mt1", "mt2", "mt3"],
    overlay=False,
    control=True,
).add_to(map)

folium.raster_layers.TileLayer(
    tiles="http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
    attr="google",
    name="google street view",
    max_zoom=20,
    subdomains=["mt0", "mt1", "mt2", "mt3"],
    overlay=False,
    control=True,
).add_to(map)


folium.raster_layers.WmsTileLayer(
    url="http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi",
    name="test",
    fmt="image/png",
    layers="nexrad-n0r-900913",
    attr=u"Weather data © 2012 IEM Nexrad",
    transparent=True,
    overlay=True,
    control=True,
).add_to(map)

folium.TileLayer('openstreetmap').add_to(map)
folium.TileLayer('stamentoner').add_to(map)
folium.TileLayer('stamenterrain').add_to(map)
folium.TileLayer('stamenterrain').add_to(map)
folium.LayerControl().add_to(map)

# map.add_child(folium.LatLngPopup())
# map.add_child(folium.ClickForMarker(popup="Waypoint"))

map.save('export_localizacao.html')
