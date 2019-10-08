import pandas as pd
from matplotlib import pyplot as plt

datos = pd.read_excel('Roedores.xls', index_col=0)
print(list(datos.columns.values))
datos.columns = ['TITULO', 'DESCRIPCION', 'INSTITUCION', 'FUENTE', 'URL', 'CONTACTO', 'LATITUD', 'LONGITUD', 'MES', 'ANIO', 'GEOMETRIA', 'ALTURA-MSNM', 'NRO-TAXA']

#MES_CONSULTA = "Diciembre"

##CONSULTA = pd.value_counts(datos['URL']) #Digamos que Categorizo...
##print ("---------------------------------------------------------------")
##print (CONSULTA)
##print ("---------------------------------------------------------------")
##print ("Registros (Filas) : ", len(CONSULTA))
##print ("---------------------------------------------------------------")
##CONSULTA.to_csv('CONTACTO-01.tsv', sep='\t', index=True, header=True)

plot_torta = datos['NRO-TAXA'].value_counts().plot(kind='pie', autopct='%.2f', figsize=(8, 8),
                                            title='NRO-TAXA-ROEDORES')
plt.show()


##CONSULTA = input("Institucion a Consultar : ") 
##resultado = datos.loc[datos["INSTITUCION"] == CONSULTA,["MES","DESCRIPCION","NRO-TAXA", "CONTACTO"]]
##
##
##print ("Institucion :", CONSULTA)
##
##print (resultado)
##print ("---------------------------------------------------------------")
##print ("Registros (Filas) : ", len(resultado))
##print ("---------------------------------------------------------------")
##
##resultado.to_csv('INSTITUCION-02.tsv', sep='\t', index=True, header=True)
##
