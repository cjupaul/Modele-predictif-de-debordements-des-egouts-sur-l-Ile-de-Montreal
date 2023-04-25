import pandas as pd

# Importation des données de débordements provenant de la ville de Montréal

df_2017 = pd.read_csv('./web_data_inputs/debordements2017.csv',sep=',')
df_2018 = pd.read_csv('./web_data_inputs/debordements2018.csv',sep=',')
df_2019 = pd.read_csv('./web_data_inputs/debordements2019.csv',sep=',')
df_2020 = pd.read_csv('./web_data_inputs/debordements2020.csv',sep=',')

# Ajustements des données 

df_2017_modif=df_2017
df_2017_modif=df_2017_modif.rename(columns={"NON SUIVI": "Non suivi"})
df_2017_modif=df_2017_modif.rename(columns={"Précipitation Type": "Précipitations Type"})
df_2017_modif=df_2017_modif.rename(columns={"Précipitation Hauteur": "Précipitations Hauteur"})
df_2017_modif=df_2017_modif.rename(columns={"Surverse Durée": "Surverses Durée"})
df_2017_modif=df_2017_modif.rename(columns={"Surverse Code contexte": "Surverses Code contexte"})
df_2017_modif=df_2017_modif.rename(columns={"Surverse Commentaire": "Surverses Commentaire"})

df_2018_modif=df_2018
df_2018_modif=df_2018_modif.rename(columns={"Surverses Rejet": "DonnéeRejet"})

df_2019_modif=df_2019
df_2019_modif=df_2019_modif.rename(columns={"NON SUIVI": "Non suivi"})

df_2020_modif=df_2020
df_2020_modif=df_2020_modif.rename(columns={"NON SUIVI": "Non suivi"})

order = [0,1,2,3,4,5,6,7,9,10,11,8,12,13,14] # ordonner les colonnes
df_2019_modif = df_2019_modif[[df_2019_modif.columns[i] for i in order]]

order2 = [0,1,2,3,4,5,6,7,9,10,11,8,12,13] # ordonner les colonnes
df_2020_modif = df_2020_modif[[df_2020_modif.columns[i] for i in order2]]

df_2020_modif['Surverses Commentaire'] = ''

# Importation des données de géolocalisation des stations provenant de la ville de Montréal 

df_ouvrage=pd.read_csv('./web_data_inputs/ouvrages-surverses.csv',sep=',')

df_2017_05=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_05-2017_P1H.csv')
df_2017_06=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_06-2017_P1H.csv')
df_2017_07=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_07-2017_P1H.csv')
df_2017_08=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_08-2017_P1H.csv')
df_2017_09=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_09-2017_P1H.csv')
df_2017_10=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_10-2017_P1H.csv')

df_2018_05=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_05-2018_P1H.csv')
df_2018_06=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_06-2018_P1H.csv')
df_2018_07=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_07-2018_P1H.csv')
df_2018_08=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_08-2018_P1H.csv')
df_2018_09=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_09-2018_P1H.csv')
df_2018_10=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_10-2018_P1H.csv')

df_2019_05=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_05-2019_P1H.csv')
df_2019_06=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_06-2019_P1H.csv')
df_2019_07=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_07-2019_P1H.csv')
df_2019_08=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_08-2019_P1H.csv')
df_2019_09=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_09-2019_P1H.csv')
df_2019_10=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_10-2019_P1H.csv')

df_2020_05=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_05-2020_P1H.csv')
df_2020_06=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_06-2020_P1H.csv')
df_2020_07=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_07-2020_P1H.csv')
df_2020_08=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_08-2020_P1H.csv')
df_2020_09=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_09-2020_P1H.csv')
df_2020_10=pd.read_csv('./web_data_inputs/en_climate_hourly_QC_702S006_10-2020_P1H.csv')

# Fusion des données annuelles de débordement provenant de la ville de Montréal

frames = [df_2017_modif, df_2018_modif, df_2019_modif,df_2020_modif]

df_all_year_train = pd.concat(frames,axis=0,ignore_index=True)

# Fusion des données de géolocalisation avec les données  annuelles de débordement provenant de la ville de Montréal

df_ouvrage_rename=df_ouvrage
df_ouvrage_rename=df_ouvrage_rename.drop_duplicates(subset=['ID_ouvrage'])
df_all_year_ouvrage_train = pd.merge(df_all_year_train, df_ouvrage_rename,left_on="Site No", right_on="ID_ouvrage", how="inner",validate='many_to_one')

# Fusion des données précédentes avec les données horaires météorologiques

df_meteo_all_year_train=pd.DataFrame([])
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_05],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_06],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_07],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_08],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_09],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2017_10],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_05],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_06],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_07],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_08],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_09],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2018_10],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_05],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_06],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_07],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_08],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_09],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2019_10],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_05],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_06],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_07],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_08],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_09],ignore_index=True)
df_meteo_all_year_train=pd.concat([df_meteo_all_year_train,df_2020_10],ignore_index=True)

df_meteo_all_year_train['Date/Time (LST)_2'] = pd.Index(map(lambda x : str(x)[:-6], df_meteo_all_year_train['Date/Time (LST)'] ))

df_merge = pd.merge(df_meteo_all_year_train, df_all_year_ouvrage_train,left_on="Date/Time (LST)_2", right_on="Date",how="inner",validate='many_to_many')

df_merge_stations=df_merge.loc[(df_merge['Site No'] == '3260-01D')  |  (df_merge['Site No'] == '3350-07D') |  
                        (df_merge['Site No'] == '4240-01D') |  (df_merge['Site No'] == '4350-01D') |  (df_merge['Site No'] == '4380-01D')]

# Retraits de variables

df=df_merge_stations
df=df[['Date/Time (LST)','Year','Month','Day','Time (LST)','Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Wind Spd (km/h)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Site No','Précipitations Hauteur','Précipitations Type','Surverses Durée','Non suivi',
                        'Surverses Code contexte','DonnéeRejet','Surverses Commentaire','Trop-Plein Lat','Trop-Plein Lon']]

df = df.reset_index(drop=True)

# Feature engineering et nettoyage

df['Surverses Durée']=df['Surverses Durée'].str.replace(',','.')
df['Surverses Durée']=df['Surverses Durée'].astype(float)

df['Précipitations Type']=df['Précipitations Type'].str.replace(' ','0')
df['Précipitations Type'] = df['Précipitations Type'].fillna('0')

i=0
for h in df["Précipitations Type"]:
    if h == 'P':
        df["Précipitations Type"][i] = 1
    else:
        df["Précipitations Type"][i] = 0
    i=i+1

i=0
for h in df["Surverses Durée"]:
    if h > 0:
        df["Surverses Durée"][i] = 1
    else:
        df["Surverses Durée"][i] = 0
    i=i+1

# Ordonner les variables afin que ça soit plus facile à lire et changer le nom de Surverses Durée pour Surverse

order2 = [13,0,1,2,3,4,5,6,7,8,10,11,12,17,18,19,20,21,22,14,15,16] # ordonner les colonnes
df = df[[df.columns[i] for i in order2]]
df=df.rename(columns={"Surverses Durée": "Surverse"})
df['Précipitations Type'] = pd.to_numeric(df['Précipitations Type'])
df['Surverse'] = pd.to_numeric(df['Surverse'])


df.to_csv('./data_preprocessing_outputs/df.csv',index=False)

if __name__ == "__main__":
    print(df)