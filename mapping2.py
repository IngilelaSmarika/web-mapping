import folium
from pandas import read_csv
data = read_csv("population.txt")
lat  = list(data["LAT"])
lon = list(data["LON"])
location = list(zip(lat,lon))
PopTotal = list(data["POPTOTAL"])
PopMale = list(data["POPMALE"])
PopFemale = list(data["POPFEMALE"])
PopKids= list(data["POPKIDS"])
Educated_men=list(data["EDUCATEDMEN"])
Educated_Women=list(data["EDUCATEDWOMEN"])
Uneducated_men=list(data["UNEDUCATEDMEN"])
Uneducated_women=list(data["UNEDUCATEDWOMEN"])
v_location = list(data["LOCATION"])
Death_cases=list(data["DEATHCASES"])

description = list(zip(PopTotal,PopMale,PopFemale,PopKids,v_location))
population_desp = dict(zip(location,description))
map = folium.Map((-28,24),zoom_start=7,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "Population Information")
html = """<h4>Population information:</h4>
PopTotal: %s <br>
PopMale  : %s<br>
PopFemale : %s <br>
PopKids: %s <br> 
"""
for x in population_desp.keys():
    iframe = folium.IFrame(html=html % ( str(population_desp[x][0]) ,str(population_desp[x][1]),str(population_desp[x][2]), str(population_desp[x][3])), width=300, height=100)
    fg.add_child(folium.Marker(location= x, popup= folium.Popup(iframe),parse_html=True ,icon=folium.Icon(color="blue")))


fgp=folium.FeatureGroup(name="Population Float")

fgp.add_child(folium.GeoJson(data=open('world.Json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'yellow'if x['properties']['POP2005']<10000000 else 'orange'
 if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


fge=folium.FeatureGroup(name="Literacy Information")
Literacy=list(zip(Educated_men,Educated_Women,Uneducated_men,Uneducated_women))
Linfo=dict(zip(location,Literacy))

html = """<h4>Literacy information:</h4>
Educated_men: %s <br>
Educated_Women : %s<br>
Uneducated_men : %s <br>
Uneducated_women: %s <br> 
"""
for y in Linfo.keys():
    iframe1 = folium.IFrame(html=html % ( str(Linfo[y][0]),str(Linfo[y][1]),str(Linfo[y][2]),str(Linfo[y][3])), width=300, height=100)
    fge.add_child(folium.Marker(location=y,radius=7,popup= folium.Popup(iframe1),parse_html=True,icon=folium.Icon(color="darkpurple")))


fgd=folium.FeatureGroup(name="Death Cases")
Dinfo=dict(zip(location,Death_cases))
html = """<h4>Death cases:</h4>
Death_Cases: %s <br>
"""
for z in Dinfo.keys():
    iframe1 = folium.IFrame(html=html % ( str(Dinfo[z])), width=300, height=100)
    fgd.add_child(folium.Marker(location=z,radius=7,popup= folium.Popup(iframe1),parse_html=True,icon=folium.Icon(color="red")))


map.add_child(fg)
map.add_child(fgp)
map.add_child(fge)
map.add_child(fgd)
map.add_child(folium.LayerControl())
map.save("Mapping2.html")