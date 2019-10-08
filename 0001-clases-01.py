class Alumno:
	nombre = ""
	apellido = ""
	dni = 0
	nota1 = 0.0
	nota2 = 0.0
	nota3 = 0.0
	
	def promedio (self):
		return (self.nota1+self.nota2+self.nota3)/3
		
	def aprobado (self):
		return self.promedio()>=6.0

Manuel=Alumno()		
Manuel.nombre="Jose Manuel"
Manuel.apellido="ENCALADA"
Manuel.dni = 22420860
Manuel.nota1= 7
Manuel.nota2=8
Manuel.nota3=9

print ("Me llamo:", Manuel.nombre, Manuel.apellido)
print ("DNI:", Manuel.dni)
print ("Mi Promedio es:", Manuel.promedio())
print ("Estado de Aprobado:", Manuel.aprobado())
