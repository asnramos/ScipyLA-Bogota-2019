import pandas as pd
from matplotlib import pyplot as plt

datos = pd.read_excel('Jujuy-Padron-2019.xlsx')

datos.columns = ['TIPO DE EJEMPLAR', 'MATRICULA', 'APELLIDO', 'NOMBRE', 'CLASE', 'GENERO', 'DOMICILIO', 'SECCION', 'CIRCUITO', 'MESA',
                 'ORDEN', 'TX_CODIGO_TIPO_ELECTOR', 'TX_SECC_NUMERO', 'TX_CIRC_NUMERO', 'TX_COLOR']

CONSULTA = pd.value_counts(datos['SECCION']) #Digamos que Categorizo...

print ("---------------------------------------------------------------")
print (CONSULTA)
print ("---------------------------------------------------------------")
print ("Registros (Filas) : ", len(CONSULTA))
print ("---------------------------------------------------------------")
CONSULTA.to_csv('VOTANTES-SECCION-PADRON-JUJUY -02.tsv', sep='\t', index=True, header=True)

# Gráfico de barras votantes x depto Jujuy
plot_barras = datos['SECCION'].value_counts().plot(kind='bar', title='Votantes por SECCION Departamentos Jujuy')
plot_barras.set_ylabel('Cant de votantes')
plot_barras.set_xlabel('SECCION Deptos Jujuy')

#Grafico de tortas votantes x depto Jujuy
#plot_torta = datos['SECCION'].value_counts().plot(kind='pie', autopct='%.2f', figsize=(8, 8),
#                                            title='Votantes por Departamentos Jujuy')
plt.show()



#print('Promedio : ', datos['NRO-TAXA'].mean())
#print ('Promedio (2 decimales) : ', str(round(datos['NRO-TAXA'].mean(),2))) #redondeo en 2



