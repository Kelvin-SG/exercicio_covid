#Biblioteca para trabalhar com DataFrame
import pandas as pd

#Lendo/Abrindo o arquivo .csv
covid = pd.read_csv('/home/virtual/Desktop/Exercicio_Hbase/covid/covid_19_data.csv', sep=',')

#apagando todos regitros com valores nullos
covid19 = covid.dropna()

#exportando em um novo arquivo .csv
covid19.to_csv('/home/virtual/Desktop/Exercicio_Hbase/covid/covid19.csv', index=False, sep=',')

#Proximos passos:
#Commitar e enviar para o git;
#Baixar na maquina Cloudera