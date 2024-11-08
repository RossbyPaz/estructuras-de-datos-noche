#Ejemplo con Diccionarios

diccionario = {}  #diccionario vacio
puertos = {
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    3306: "My Sql",
    1526: "Oracle"

}
print(puertos[22])
puertos1 = {
    22: "SSH",
    80: "Http"

}
puertos2 = {
    53: "DNS",
    443: "Https"
}
print(puertos1)
puertos1.update(puertos2)  #Actualizar el diccionario
print(puertos1)

#Eliminar un elemento dell diccionario
calificaciones = {
    "Alumno1": 5,
    "Alumno2": 4,
    "Alumno3": 3,
    "Alumno4": 2,
}
print(calificaciones)
del calificaciones["Alumno3"] #eliminar una pareja del diccionario
print(calificaciones)

#Iterar en un diccionario
dicPuerto = {
    22:"SSH",
    23:"Telnet",
    80:"Http"
}
for x,y in dicPuerto.items():
    print(x, "->", y)