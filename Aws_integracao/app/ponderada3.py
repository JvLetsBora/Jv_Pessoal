
# importações necessarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

df_read = pd.read_csv('./Activity_history.csv')

df_read.isna().sum()

df_traino = df_read.dropna()

df_traino

df_traino["App name"].unique()



colunas_interresse = [
    "WhatsApp", "Instagram", "Gmail", "YouTube"
]

novo_df = df_traino.groupby(['App name', 'Date'])['Duration'].sum().reset_index()

segundos = df_traino["Duration"]


segundos = []
for time in df_traino["Duration"]:
  a = time.split(":")
  b = (int(a[0])*100000) + (int(a[1])*1000) + (int(a[2])*10)
  segundos.append(b)

df_traino["Duration"] = segundos

df_traino

df_filtrado = df_traino[df_traino['App name'].isin(colunas_interresse)]

df_traino = df_filtrado


times = []
for time in df_traino["Time"]:
  a = time.split(":")
  a2 = a[2].split(" ")
  b = (int(a[0])*100000) + (int(a[1])*1000) + (int(a2[0])*10)
  times.append(b)

df_traino["Time"] = times



lb = LabelEncoder()


apps = lb.fit_transform(df_traino["App name"])
apps

df_traino["labels_app"] = apps
df_traino

oneHot = OneHotEncoder()
arr = oneHot.fit_transform(df_traino[["labels_app"]]).toarray()
arr

one_hot_df = pd.DataFrame(arr, columns=[f'App_id_{i}' for i in range(arr.shape[1])])
one_hot_df

new_df = df = pd.concat([df_traino, one_hot_df], axis=1)
new_df = new_df.drop(["App name","labels_app","Date" ],axis=1)

new_df


scaler = MinMaxScaler()

df_scaled = scaler.fit_transform(new_df[["Time"]])

df_scaled = pd.DataFrame(df_scaled, columns=["Time"])


new_df=new_df.dropna()

new_df.head(100)


X = new_df.drop('Duration', axis=1)  # Features
y = new_df['Duration']  # Target variable

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando um modelo de regressão linear
model = LinearRegression()

# Treinando o modelo
model.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliando o modelo
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

def pepiline(body):
    [528410.0, 0.0, 0.0, 1.0, 0.0]
    times = []
    a = time.split(":")
    a2 = a[2].split(" ")
    b = (int(a[0])*100000) + (int(a[1])*1000) + (int(a2[0])*10)
    times.append(b)

    data = [[
        times[0],body["WhatsApp"], body["Instagram"], body["Gmail"], body["YouTube"]
    ]]
    
    return data

def predict(a):
    y_pred = model.predict(a)
    return y_pred




