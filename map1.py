import folium
import pandas

def volcano_map():

    # Create folium HTML map and marker layer
    map = folium.Map(location=[38.626594, -98.073325], min_zoom=3, zoom_start=5, tiles='Stamen Terrain')
    fgv = folium.FeatureGroup(name='Volcanoes')
    fgp = folium.FeatureGroup(name='Population')

    # Import data from CSV and save relevant columns to lists
    data = pandas.read_csv('Volcanoes.csv')
    lat = list(data['LAT'])
    long = list(data['LON'])
    name = list(data['NAME'])
    elev = list(data['ELEV'])

    # Pass list data into create circle marker function
    for lt, ln, nm, ev in zip(lat, long, name, elev):
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill_opacity=0.7, color='grey', 
        popup=f'{nm} \n {int(ev)} m', fill_color = elevation(ev)))

    # Create population overlay layer
    fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 10000000 <=x['properties']['POP2005'] < 20000000 else 'red'}))
    

    # Apply marker feature group
    map.add_child(fgv)
    map.add_child(fgp)

    # Create a layer control panel
    map.add_child(folium.LayerControl())

    # Save as HTML file
    map.save('Map1.html')

# Return a color based on elevation
def elevation(int):
    if int < 1000:
        return 'green'
    elif 1000 < int < 3000:
        return 'orange'
    else:
        return 'red'


volcano_map()