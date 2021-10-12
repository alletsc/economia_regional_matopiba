import pandas as pd
import numpy as np
import folium


brasil = folium.Map(
    # Coordenadas retiradas do Google Maps
    location=[-16.1237611, -59.9219642],
    zoom_start=4)

suape = folium.CircleMarker(location=[-8.3944,  -34.9741],
                            popup='Porto de Suape',
                            tooltip='Porto de Suape',
                            icon=folium.Icon(color='blue')
                            ).add_to(brasil)

itaqui = folium.Marker(location=[-2.5776,  -44.3673],
                             popup='Porto de Itaqui',
                             tooltip='Porto de Itaqui',
                             icon=folium.Icon(color='green', icon='ship',prefix='fa')
                             ).add_to(brasil)

pecem = folium.CircleMarker(location=[-3.5495,  -38.8108],
                            popup='Porto de Pécem',
                            tooltip='Porto de Pécem',
                            icon=folium.Icon(color='red')
                            ).add_to(brasil)

folium.TileLayer('openstreetmap').add_to(brasil)
folium.TileLayer('stamentoner').add_to(brasil)
folium.TileLayer('stamenterrain').add_to(brasil)

folium.TileLayer('cartodbpositron').add_to(brasil)

folium.LayerControl().add_to(brasil)

brasil.save('portos_proximos_matopiba.html')
