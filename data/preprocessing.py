import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# Rejet de variables

df=pd.read_csv('./data_preprocessing_outputs/df.csv')
df_preprocessing=df.drop(['Date/Time (LST)','Non suivi','Surverses Code contexte','DonnéeRejet','Surverses Commentaire'], axis=1)

# Séparer nos données en données « test » et données « d'entrainement ». Les données « test » seront les données de 2020. De plus, d'autres variables sont enlevées.

df_train=df_preprocessing[df_preprocessing['Year']<2019]
df_valid=df_preprocessing[df_preprocessing['Year']==2019]
df_test=df_preprocessing[df_preprocessing['Year']==2020]

df_train=df_train.drop(['Trop-Plein Lat'], axis=1)
df_valid=df_valid.drop(['Trop-Plein Lat'], axis=1)
df_test=df_test.drop(['Trop-Plein Lat'], axis=1)


df_train=df_train.drop(['Trop-Plein Lon'], axis=1)
df_valid=df_valid.drop(['Trop-Plein Lon'], axis=1)
df_test=df_test.drop(['Trop-Plein Lon'], axis=1)

df_train=df_train.drop(['Year'], axis=1)
df_valid=df_valid.drop(['Year'], axis=1)
df_test=df_test.drop(['Year'], axis=1)

df_train=df_train.drop(['Time (LST)'], axis=1)
df_valid=df_valid.drop(['Time (LST)'], axis=1)
df_test=df_test.drop(['Time (LST)'], axis=1)

df_train = df_train.reset_index(drop=True)
df_valid = df_valid.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Appliquer le Label encoding sur nos variables catégorielles

label_encoder=LabelEncoder()
encoded_labels_1 = label_encoder.fit_transform(df_train['Surverse'])
encoded_labels_2 = label_encoder.fit_transform(df_valid['Surverse'])
encoded_labels_3 = label_encoder.fit_transform(df_test['Surverse'])

encoded_labels_4 = label_encoder.fit_transform(df_train['Site No'])
encoded_labels_5 = label_encoder.fit_transform(df_valid['Site No'])
encoded_labels_6 = label_encoder.fit_transform(df_test['Site No'])

# Normaliser les données

df_train['Surverse']=encoded_labels_1
df_valid['Surverse']=encoded_labels_2
df_test['Surverse']=encoded_labels_3

df_train['Site No']=encoded_labels_4
df_valid['Site No']=encoded_labels_5
df_test['Site No']=encoded_labels_6

# Rejet de variables

scaler=MinMaxScaler()
scaler_1 = scaler.fit_transform(df_train[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']])
scaler_2 = scaler.fit_transform(df_valid[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']])
scaler_3 = scaler.fit_transform(df_test[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']])

df_train[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']]=scaler_1
df_valid[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']]=scaler_2
df_test[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']]=scaler_3

# Transformation données pour la carte géographique

df=df.drop(['Non suivi','Surverses Code contexte','DonnéeRejet','Surverses Commentaire'], axis=1)
df_test_2020=df[df['Year']==2020]
df_test_2020=df_test_2020.drop(['Year'], axis=1)
df_test_2020=df_test_2020.drop(['Time (LST)'], axis=1)
df_test_2020 = df_test_2020.reset_index(drop=True)
encoded_labels_2 = label_encoder.fit_transform(df_test_2020['Surverse'])
encoded_labels_4 = label_encoder.fit_transform(df_test_2020['Site No'])
df_test_2020['Surverse']=encoded_labels_2
scaler_2 = scaler.fit_transform(df_test_2020[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']])
df_test_2020[['Temp (°C)','Rel Hum (%)','Precip. Amount (mm)','Wind Dir (10s deg)','Stn Press (kPa)',
                        'Hmdx','Wind Chill','Précipitations Hauteur']]=scaler_2
df_test_2020['Date/Time (LST)'] = pd.Index(map(lambda x : str(x)[:-6], df_test_2020['Date/Time (LST)'] ))

# Enregistrer csv file train/valid/test/data_map

df_train.to_csv('./data_preprocessing_outputs/data_train.csv',index=False)
df_valid.to_csv('./data_preprocessing_outputs/data_valid.csv',index=False)
df_test.to_csv('./data_preprocessing_outputs/data_test.csv',index=False)
df_test_2020.to_csv('./data_preprocessing_outputs/data_test_2020.csv',index=False)

if __name__ == "__main__":
    print('df_train',df_train)
    print('df_valid',df_valid)
    print('df_test',df_test)