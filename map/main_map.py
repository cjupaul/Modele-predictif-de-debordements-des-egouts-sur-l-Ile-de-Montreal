import folium
from folium.plugins import MarkerCluster
import pandas as pd
import subprocess

def main():

    subprocess.run(["python", "preprocessing_map.py"])

    df_map_f2 = pd.read_csv('./data_map_preprocessing_outputs/df_map_folium.csv')

    #@title Veuillez entrer une journée afin de visualiser les stations à risque

    Jour = input('Veuillez entrer une date entre le 1er mai et le 31 octobre dans le format suivant: MM-JJ ') #@param {type:"date"}

    # Map
    icon_create_function = """
        function(cluster) {
        var childCount = cluster.getChildCount();
        var c = ' marker-cluster-';

        if (childCount < 300) {
            c += 'small';
        } else if (childCount < 300) {
            c += 'small';
        } else {
            c += 'small';
        }

        return new L.DivIcon({ html: '<div><span>' + childCount + '</span></div>', className: 'marker-cluster' + c, iconSize: new L.Point(40, 40) });
        }
        """
    df_map_f=df_map_f2
    df_map_f=df_map_f[df_map_f['Date/Time (LST)']== str(2020) + "-" + str(Jour)]
    map = folium.Map(location=[45.535994, -73.614798],zoom_start=11, tiles='cartodbpositron', control_scale=True)

    marker_cluster = MarkerCluster(icon_create_function=icon_create_function).add_to(map)

    for idx, row in df_map_f.iterrows():
        if(row['y_pred_agg'] < 0.15):
            marker_active  = folium.Marker([row['Trop-Plein Lat'], row['Trop-Plein Lon']],popup='Site_No:<br>{}<br>Proba:{}%'.format(row['Site No'], round(row['y_pred_agg']*100,2)),icon = folium.Icon(color='green',icon='ok-sign')).add_to(marker_cluster)
        
        elif row['y_pred_agg'] < 0.50 :
            folium.Marker([row['Trop-Plein Lat'], row['Trop-Plein Lon']],popup='Site_No:<br>{}<br>Proba:{}%.format'.format(row['Site No'], round(row['y_pred_agg']*100,2)),icon = folium.Icon(color='orange',icon='exclamation-sign')).add_to(map)

        else:
            folium.Marker([row['Trop-Plein Lat'], row['Trop-Plein Lon']],popup='Site_No:<br>{}<br>Proba:{}%'.format(row['Site No'], round(row['y_pred_agg']*100,2)),icon = folium.Icon(color='red',icon='exclamation-sign')).add_to(map)

    # save map to html file
    map.save('./map_outputs/geographic_map.html')

if __name__ == '__main__':
    main()