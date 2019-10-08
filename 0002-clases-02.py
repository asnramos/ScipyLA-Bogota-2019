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

Diego=Alumno()		
Diego.nombre="Diego Exequiel"
Diego.apellido="RAMIREZ SCOVOTTI"
Diego.dni = 22420860
Diego.nota1= 7
Diego.nota2=8
Diego.nota3=9

print ("------------------------------------------------------------------------------------------------------------------")
print ("Me llamo:", Diego.nombre, Diego.apellido)
print ("DNI:", Diego.dni)
print ("Mi Promedio es:", Diego.promedio())
print ("Estado de Aprobado:", Diego.aprobado())
print ("------------------------------------------------------------------------------------------------------------------")

Ariel=Alumno()		
Ariel.nombre="Ariel Silvio Norberto"
Ariel.apellido="RAMOS"
Ariel.dni = 31518323
Ariel.nota1= 5
Ariel.nota2=6
Ariel.nota3=4

print ("------------------------------------------------------------------------------------------------------------------")
print ("Me llamo:", Ariel.nombre, Ariel.apellido)
print ("DNI:", Ariel.dni)
print ("Mi Promedio es:", Ariel.promedio())
print ("Estado de Aprobado:", Ariel.aprobado())
print ("------------------------------------------------------------------------------------------------------------------")
