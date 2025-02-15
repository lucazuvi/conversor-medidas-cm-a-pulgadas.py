import pandas as pd 

#Dataframe es la info basica con el nombre de las piezas y cm para poder armar el Excel

data = {
    'Piezas: ': ['Pata','Tablero','Puerta','Estante','Panel lateral'],
    'Centimetro: ': [40,120,60,30,180]
}

df =pd.DataFrame(data)

#Guardar Dataframe en in archivo Excel

df.to_excel('muebles_medidas.xlsx',index=False)