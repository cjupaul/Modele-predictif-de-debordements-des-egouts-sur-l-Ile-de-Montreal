import torch
from tqdm.auto import tqdm 
import pandas as pd
from LSTM import StationPredictor 
from parameters import parameters as p
from dataset import StationDataset
from data_module import create_sequences

predictions_prob_tensor=[]

trained_model = StationPredictor.load_from_checkpoint("./model_inputs/" + p["model_name"] + ".ckpt")

data_test = pd.read_csv('./data_inputs/data_test.csv')
data_test_sequence = StationDataset(create_sequences(data_test, p["Surverse"], p["sequence_lenght"]))

for item in tqdm(data_test_sequence):
  sequence = item["sequence"]

  _, output =trained_model(torch.unsqueeze(sequence,dim=0))
  prediction = torch.nn.functional.softmax(output, dim=1)
  predictions_prob_tensor.append(prediction)

#Prendre la bonne probabilité dans le tensor concernant la possibilité d'un surversement

predictions_prob=[]
i=0
for i in range(len(predictions_prob_tensor)):
  predictions_prob.append(round(predictions_prob_tensor[i][0][1].detach().numpy().tolist(),2))
  i=i+1

#Puisque notre base de données s’exprime en séquences horaires, il sera nécessaire de créer un dataframe 
# permettant de mettre le tous de manière quotidienne. Nous cherchons à exprimer les probabilités de survenance de manière quotidienne.

data_test_2020 = pd.read_csv('./data_inputs/data_test_2020.csv')

df_clean_1 = pd.read_csv('./data_inputs/df.csv')

df_test_1=data_test_2020[p["sequence_lenght"]:]
df_test_1 = df_test_1.reset_index(drop=True)

y_pred=pd.DataFrame(predictions_prob, columns=['y_pred'])
df_map=pd.concat([df_test_1,y_pred],axis=1)

agg_df_y_pred=df_map.groupby(['Date/Time (LST)','Site No']).max().reset_index()
agg_df_y_pred=agg_df_y_pred.rename(columns={"y_pred": "y_pred_agg"})
agg_df_y_pred=agg_df_y_pred[['Site No','Date/Time (LST)','y_pred_agg']]
agg_df_y_pred['Trop-Plein Lat']=agg_df_y_pred['Site No']
agg_df_y_pred['Trop-Plein Lon']=agg_df_y_pred['Site No']
agg_df_y_pred["Trop-Plein Lat"].replace({"4240-01D": "45.650719","4350-01D": "45.499070","4380-01D": "45.467749","3260-01D": "45.650719","3350-07D": "45.546148"}, inplace=True)
agg_df_y_pred["Trop-Plein Lon"].replace({"4240-01D": "-73.487750","4350-01D": "-73.554988","4380-01D": "-73.563688","3260-01D": "-73.580273","3350-07D": "-73.692084"}, inplace=True)

df_map_folium=agg_df_y_pred
df_map_folium['Trop-Plein Lat'] = pd.to_numeric(df_clean_1['Trop-Plein Lat'])
df_map_folium['Trop-Plein Lon'] = pd.to_numeric(df_clean_1['Trop-Plein Lon'])

df_map_folium.to_csv("./data_map_preprocessing_outputs/df_map_folium.csv",index=False)
