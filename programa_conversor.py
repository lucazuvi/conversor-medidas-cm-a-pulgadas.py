import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# Leer el Excel

df = pd.read_excel("muebles_medidas.xlsx")

# Agregar una columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm/2.54

df['pulgadas'] = df['Centimetro: '].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print('Conversion realizada y guardada en: "muebles_medidas_convertidas.xlsx".')

print(df.columns)
