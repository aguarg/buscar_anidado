# Función que devuelve el valor de la llave que queramos en un diccionario.
# La idea es no tener que buscar una por una las múltiples rutas en un diccionario anidado para acceder al valor que queramos.


# Este es un diccionario de ejemplo para probar la función:
diccionario_ejemplo = {
	"llave A nivel 1": "valor A nivel 1",
	"llave B nivel 1": "valor B nivel 1",
	"llave C nivel 1": { 
		"llave A nivel 2": "valor A nivel 2", 
		"llave B nivel 2": "valor B nivel 2",
		"llave C nivel 2": {
			"llave A nivel 3": "valor A nivel 3",
			"llave B nivel 3": {
				"llave A nivel 4": "valor mas profundo"
			}
		}
	}
}






def buscar_valor(diccionario, llave_buscada):

"""
Funcion para buscar el valor de la llave.
Parámetros:
- diccionario: es el diccionario por el que queremos iterar.
- llave_buscada: es el nombre de la llave que buscamos y de la cual vamos a obtener su valor.

"""



    for llave, valor  in diccionario.items():  #.items() devuelve los pares key:value como una lista en una tupla (ver nodo)
        if llave == llave_buscada:
            return valor


        
        elif isinstance(valor, dict): # si valor es del type dict (es decir, si el type de valor es un diccionario):
            found = buscar_valor(valor, llave_buscada)  # ahora usa la función de forma recursiva, pero esta vez el argumento "diccionario"
            #es reemplazado por el valor "valor" de la llave (es decir un diccionario anidado) y llave_buscada como el segundo argumento.
            
            if found is not None:  #si la función recursiva no encontró un diccionario como valor (not None):
                return found





# Probamos la función para ver si obtiene el valor anidado mas profundo:
buscar_valor(diccionario_ejemplo, "llave A nivel 4")

# si funciona bien, devuelve "valor mas profundo"
