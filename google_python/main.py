import webbrowser

import geopandas
import shapely
import simplekml

kml = simplekml.Kml()

# lon, lat, altura opcional
kml.newpoint(name="Fazenda do Clariano", coords=[(-47.260443, -18.768914)])

kml.document.name = "Talhão"

# salva o arquivo .kml
kml.save("D:\\Informatica\\Python\\google_python\\exemplo-01.kml")

# abrir arquivo
webbrowser.open('D:\\Informatica\\Python\\google_python\\exemplo-01.kml')
