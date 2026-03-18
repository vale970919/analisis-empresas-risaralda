# %%
#Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Cargar el archivo CSV
archivo_csv=r"C:\Users\vacev\OneDrive\Escritorio\INGENIERIA INDUSTRIAL\SEMESTRE 6\DATA EXPERIENCE\empresas_mas_grandes_de_risaralda.csv"
df = pd.read_csv(archivo_csv)
# Ver primeras filas
print(df.head())

# %%
#Dimensiones del DataFrame
print(df.shape)

# %%
#Tipos de variables
print(df.info())


# %%
#Valores nulos
print(df.isnull().sum())

# %%
# limpiar la columna ingresos
df["INGRESOS OPERACIONALES"] = df["INGRESOS OPERACIONALES"].replace('[\$,]', '', regex=True)

# convertir a número
df["INGRESOS OPERACIONALES"] = pd.to_numeric(df["INGRESOS OPERACIONALES"], errors="coerce")
# limpiar símbolos y comas
df["INGRESOS OPERACIONALES"] = df["INGRESOS OPERACIONALES"].replace('[\$,]', '', regex=True)

# convertir a número
df["INGRESOS OPERACIONALES"] = pd.to_numeric(df["INGRESOS OPERACIONALES"], errors='coerce')

# %%
#Duplicados 
print(df.duplicated().sum())


# %%
# Convertir datos a numéricos
df["TOTAL ACTIVOS"] = df["TOTAL ACTIVOS"].replace('[\$,]', '', regex=True)
df["TOTAL ACTIVOS"] = pd.to_numeric(df["TOTAL ACTIVOS"], errors='coerce')
df["TOTAL PASIVOS"] = df["TOTAL PASIVOS"].replace('[\$,]', '', regex=True)
df["TOTAL PASIVOS"] = pd.to_numeric(df["TOTAL PASIVOS"], errors='coerce')
df["TOTAL PATRIMONIO"] = df["TOTAL PATRIMONIO"].replace('[\$,]', '', regex=True)
df["TOTAL PATRIMONIO"] = pd.to_numeric(df["TOTAL PATRIMONIO"], errors='coerce')
df["INGRESOS OPERACIONALES"] = df["INGRESOS OPERACIONALES"].replace('[\$,]', '', regex=True)
df["INGRESOS OPERACIONALES"] = pd.to_numeric(df["INGRESOS OPERACIONALES"], errors='coerce')
df["GANANCIA (PÉRDIDA)"] = df["GANANCIA (PÉRDIDA)"].replace('[\$,]', '', regex=True)
df["GANANCIA (PÉRDIDA)"] = pd.to_numeric(df["GANANCIA (PÉRDIDA)"], errors='coerce')


# %%
df["NIT"] = df["NIT"].replace(',', '', regex=True)

# %%
#Convertir año de corte a numérico
df["Año de Corte"] = df["Año de Corte"].replace(',', '', regex=True)
df["Año de Corte"] = pd.to_numeric(df["Año de Corte"])

# %%
df.to_csv("empresas_risaralda_limpio.csv", index=False)

# %%
"""Se realizó un análisis exploratorio del dataset identificando 671 registros y 14 variables relacionadas con información financiera y general de las empresas más grandes del departamento de Risaralda.
Durante la limpieza de datos se detectaron inconsistencias en variables numéricas debido a la presencia de símbolos monetarios y separadores de miles. Estos fueron eliminados para convertir las variables a formato numérico. También se verificaron valores duplicados y datos faltantes, garantizando la calidad del dataset para el análisis posterior.
"""

# %%
# limpiar espacios
df.columns = df.columns.str.strip()

# calcular media
media = df["INGRESOS OPERACIONALES"].mean()

# mediana
mediana = df["INGRESOS OPERACIONALES"].median()
# moda
moda = df["INGRESOS OPERACIONALES"].mode()

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# %%
df["INGRESOS OPERACIONALES"].head(10)

# %%
df["INGRESOS_OPERACIONALES_PESOS"] = df["INGRESOS OPERACIONALES"] * 1000000000

# %%
media = df["INGRESOS_OPERACIONALES_PESOS"].mean()
mediana = df["INGRESOS_OPERACIONALES_PESOS"].median()
moda = df["INGRESOS_OPERACIONALES_PESOS"].mode()

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# %%
"""La media de los ingresos operacionales es aproximadamente $110.551.416, lo que indica que en promedio las empresas del dataset generan alrededor de 110 millones de pesos en ingresos operacionales."""

# %%
"""La mediana es $40.000.000, lo que significa que el 50% de las empresas tienen ingresos menores a 40 millones y el otro 50% mayores a este valor."""

# %%
"""La moda es $20.000.000, lo que indica que este es el valor de ingresos operacionales que más se repite dentro del conjunto de empresas analizadas."""

# %%
# Medidas de dispersión
rango = df["INGRESOS_OPERACIONALES_PESOS"].max() - df["INGRESOS_OPERACIONALES_PESOS"].min()
varianza = df["INGRESOS_OPERACIONALES_PESOS"].var()
desviacion = df["INGRESOS_OPERACIONALES_PESOS"].std()

print("Rango:", rango)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)

# %%
"""El rango representa la diferencia entre el valor máximo y el valor mínimo de los ingresos operacionales. En este caso, la diferencia es aproximadamente 4.05 mil millones de pesos, lo que indica una gran variabilidad entre las empresas analizadas."""

# %%
"""La varianza mide la dispersión de los ingresos respecto al promedio. El valor obtenido indica que los ingresos operacionales presentan una alta variabilidad entre las empresas del dataset."""

# %%
"""La desviación estándar indica que, en promedio, los ingresos de las empresas se alejan aproximadamente 273 millones de pesos del valor medio."""

# %%
df[["INGRESOS_OPERACIONALES_PESOS",
    "TOTAL ACTIVOS",
    "TOTAL PASIVOS",
    "TOTAL PATRIMONIO"]].describe()

# %%
plt.figure(figsize=(6,4))
sns.boxplot(x=df["INGRESOS_OPERACIONALES_PESOS"])
plt.title("Outliers en ingresos operacionales")
plt.show()

# %%
plt.figure(figsize=(6,5))
sns.scatterplot(
    x=df["TOTAL ACTIVOS"],
    y=df["INGRESOS_OPERACIONALES_PESOS"]
)
plt.title("Relación entre activos e ingresos")
plt.show()

# %%
"""Se observa una relación positiva entre los activos y los ingresos operacionales. Las empresas con mayores activos tienden a generar mayores ingresos. mayor inversión → mayor capacidad productiva → mayores ingresos."""

# %%
plt.figure(figsize=(8,5))
sns.histplot(df["INGRESOS_OPERACIONALES_PESOS"], kde=True)
plt.title("Distribución de ingresos operacionales")
plt.show()

# %%
"""La distribución de los ingresos muestra que la mayoría de las empresas se concentran en rangos bajos o medios, mientras que pocas empresas presentan ingresos extremadamente altos."""

# %%
plt.figure(figsize=(8,5))
sns.histplot(df["INGRESOS_OPERACIONALES_PESOS"], kde=True)
plt.title("Distribución de los ingresos operacionales")
plt.xlabel("Ingresos operacionales (pesos)")
plt.ylabel("Frecuencia")
plt.show()

# %%
plt.figure(figsize=(6,4))
sns.boxplot(x=df["INGRESOS_OPERACIONALES_PESOS"])
plt.title("Identificación de valores atípicos en ingresos")
plt.show()

# %%
"""El gráfico permite identificar valores atípicos, correspondientes a empresas con ingresos significativamente mayores al resto."""

# %%
plt.figure(figsize=(8,5))
df["MACROSECTOR"].value_counts().plot(kind="bar")
plt.title("Número de empresas por macrosector")
plt.xlabel("Macrosector")
plt.ylabel("Cantidad de empresas")
plt.show()

# %%
plt.figure(figsize=(6,5))
sns.scatterplot(
    x=df["TOTAL ACTIVOS"],
    y=df["INGRESOS_OPERACIONALES_PESOS"]
)
plt.title("Relación entre activos e ingresos")
plt.show()

# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df[["TOTAL ACTIVOS"]]
y = df["INGRESOS_OPERACIONALES_PESOS"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

print("R2:", r2_score(y_test, predicciones))

# %%
"""El modelo de regresión lineal permite analizar cómo los activos influyen en los ingresos operacionales. Un valor de R² cercano a 1 indica que los activos explican una gran parte de la variación en los ingresos."""

# %%
plt.figure(figsize=(6,5))
plt.scatter(X_test, y_test)
plt.plot(X_test, predicciones)
plt.title("Regresión lineal: activos vs ingresos")
plt.xlabel("Activos")
plt.ylabel("Ingresos")
plt.show()


