## ZONA DE LISTAS TUPLAS SET Y DICCIONARIO
print("--------------------------------")
print (" -- FUNCIONES VERSION 2 -- ")
print ("Janna Ramirez")
celulares=["Samsung A52", "iPhone 15", "Chafa"]
perro=("Pug", "Husky", "Labrador")

# ZONA DE FUNCIONES
# LISTAS
def verlista(telefonos):
    for uncelular in telefonos: 
        print (uncelular)

# TUPLAS
def vertupla(perros):
    for unperro in perros:
        print (unperro)

# CONJUNTOS 
set = {"Manzana", "Fresa", "Cereza"}

# DICCIONARIO 
dict = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 2010
}

# LLAMADAS A FUNCIONES
# Llamada a lista
print(" -- IMPRIME CELULARES -- ")
verlista(celulares)
# Llamada a tupla
print(" -- IMPRIME RAZAS DE PERROS -- ")
vertupla(perro)
# Llamada a conjunto
print(" -- IMPRIME FRUTAS -- ")
print(set)
# Llamada a diccionario
print(" -- IMPRIME CARROS -- ")
print(dict)
print("--------------------------------")