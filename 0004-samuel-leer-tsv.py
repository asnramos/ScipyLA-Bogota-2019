import pandas as pd
from matplotlib import pyplot as plt

datos = pd.read_csv('nuevo-puntolayer-03.tsv', delimiter="\t", index_col=0, encoding='utf-8')
print(list(datos.columns.values))

#datos.columns = 

#print (datos['Publicado'])

#print (datos)

##
##--------------------------------
##['Unnamed: 0', 'Id', 'LayerId', 'UsuarioId', 'Codigo', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Url', 'Contacto', 'Latitud', 'Longitud', 'Mes', 'Anio', 'Geometria', 'Altura', 'Taxa', 'FechaCreacion', 'Publicado', 'Activo']
##>>> archivo 3
##=================== RESTART: D:/00000-SAMUEL/samuel-02.py ===================
##['Unnamed: 0', 'Id', 'LayerId', 'UsuarioId', 'Codigo', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Url', 'Contacto', 'Latitud', 'Longitud', 'Mes', 'Anio', 'Geometria', 'Altura', 'Taxa', 'FechaCreacion', 'Publicado', 'Activo']
##>>> archivo 1
##=================== RESTART: D:/00000-SAMUEL/samuel-02.py ===================
##['Id', 'LayerId', 'UsuarioId', 'Codigo', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Url', 'Contacto', 'Latitud', 'Longitud', 'Mes', 'Anio', 'Geometria', 'Altura', 'Taxa', 'FechaCreacion', 'Publicado', 'Activo']
##>>> archivo 2
##=================== RESTART: D:/00000-SAMUEL/samuel-02.py ===================
##['Id', 'LayerId', 'UsuarioId', 'Codigo', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Url', 'Contacto', 'Latitud', 'Longitud', 'Mes', 'Anio', 'Geometria', 'Altura', 'Taxa', 'FechaCreacion', 'Publicado', 'Activo']
##archivo 3 con la columna 0 indexada
