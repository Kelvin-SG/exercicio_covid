#Biblioteca para trabalhar com DataFrame
import pandas as pd

#Lendo/Abrindo o arquivo .csv
covid = pd.read_csv('/home/virtual/Desktop/Exercicio_Hbase/covid/covid_19_data.csv', sep=',')

#apagando todos regitros com valores nullos
covid19 = covid.dropna()

#susbtituir virgula na coluna Province/State por ' -' 
covid19['Province/State'].replace(',', ' -', regex=True, inplace=True) # regex=True para fazer a alteração dentro da string

#susbtituir virgula na coluna Country/Region por ' -' 
covid19['Country/Region'].replace(',', ' -', regex=True, inplace=True)

#exportando em um novo arquivo .csv
covid19.to_csv('/home/virtual/Desktop/Exercicio_Hbase/covid/covid19.csv', index=False, sep=',')

#Proximos passos:
#Commitar e enviar para o git;
#Baixar na maquina Cloudera