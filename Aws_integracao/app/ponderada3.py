import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

df_read = pd.read_csv('/content/Activity_history.csv')
df_traino = df_read.dropna()

def convert_to_24h(time_str):
    time_obj = datetime.strptime(time_str, "%I:%M:%S %p")
    return time_obj.strftime("%H:%M:%S")

def convert_to_timedelta(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

df_traino['Time'] = df_traino['Time'].apply(lambda x: convert_to_24h(x))
df_traino['Duration'] = df_traino['Duration'].apply(lambda x: convert_to_timedelta(x))
df_traino['Duration'] = df_traino['Duration'].apply(lambda x: pd.Timedelta(x).total_seconds())
colunas_interresse = [
    "WhatsApp", "Instagram", "Gmail", "YouTube"
]
df_traino = df_traino[df_traino['App name'].isin(colunas_interresse)]
df_traino.drop(columns=['Date'], inplace=True)
df_traino = pd.get_dummies(df_traino, columns=['App name'], prefix=[''])

def periodo_do_dia(hora):
    if 6 <= hora < 12:
        return 'Manhã'
    elif 12 <= hora < 18:
        return 'Tarde'
    else:
        return 'Noite'

df_traino['Periodo do Dia'] = pd.to_datetime(df_traino['Time']).dt.hour.apply(periodo_do_dia)
df_traino = pd.get_dummies(df_traino, columns=['Periodo do Dia'], prefix=[''])

X = df_traino.drop(columns=["Duration","Time"])
y = df_traino['Duration']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

def prever(body):
  predito = modelo.predict(new_data_pipeline(body))
  return predito[0]

def new_data_pipeline(data_dict):
    # Crie um DataFrame a partir do dicionário
    new_data = pd.DataFrame(data_dict)
    hora = int(new_data['Time'][0].split(':')[0])  # Extrai a hora como um número inteiro
    if 6 <= hora < 12:
        new_data['_Manhã'] = 1
    elif 12 <= hora < 18:
        new_data['_Tarde'] = 1 
    else:
        new_data['_Noite'] = 1 
    new_data = new_data.drop(columns=["Time"])
    return new_data
