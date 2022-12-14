import pandas as pd
from google.colab import drive
drive.mount('/content/drive/')

obd_sensor = pd.read_csv('/content/drive/MyDrive/TCC/trackLog-2022-set-03_08-26-06.csv')

obd_sensor

"""Iremos fazer algumas análises baseados nos dados obtidos com o auxilio do sistema de scanner veicular OBDII, os dados mostram uma viagem da zona sul de Natal, saindo do bairro planalto para o bairro Igapó na zona norte da cidade, após essas análises mostraremos os resultados em gráficos que nós ajudarão a inferir alguns resultados, como por exemplo a velocidade da viagem, o consumo do veículo entre outras informações.
O veículo utilizado foi um Onix da marca Chevrolet ano 2019 com 6 marchas, 1.0 e com 153 mil km rodados.
"""

#Limpeza dos dados
#Mostrarei duas maneiras de verificar se existe dados faltantes e a quantidade de dados faltantes do coluna.
#primeiro com a biblioteca missingno
import missingno as msno
msno.matrix(obd_sensor)

#Segunda maneira sem o auxilio de bibliotecas
df_missing = obd_sensor.isnull().sum()
df_missing

"""Com a etapa de limpeza garantimos que não existe dados faltantes e podemos seguir com nossa análise.
A partir daqui devemos ter em mente quais perguntas gostariamos de responder com a análise dos dados.
"""

#Conhecendo melhor o dataset
obd_sensor.columns.values

#Média do consumo instânea
df_avg_kpl = obd_sensor['Kilometers Per Litre(Instant)(kpl)'].mean()
df_avg_kpl

#Média de CO2 emitido, em g/km
df_avg_CO = obd_sensor['CO₂ in g/km (Average)(g/km)'].max()
df_avg_CO

#Velocidade média, em Km/h
df_avg_speed = obd_sensor['Average trip speed(whilst stopped or moving)(km/h)'].max()
df_avg_speed

#Combustível utilizado, em litros
df_avg_fuel_used = obd_sensor['Fuel used (trip)(gal)'].mean()
df_avg_fuel_used*3.7

#Distância da viagem, em Km
df_distance = obd_sensor['Trip distance (stored in vehicle profile)(km)'].max()
df_distance

#tempo da viagem, em minutos
df_trip_time = obd_sensor['Trip Time(Since journey start)(s)'].max()
df_trip_time/60
