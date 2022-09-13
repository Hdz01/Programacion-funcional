#n1 = 10
#msg = "Hola"

#print(n1,msg)
#print(str(n1)+msg)

#fstring
#print(f"{n1} {msg}")

#Hacer una funcion que reciba el nombre de una persona 
#El año de nacimiento y el año actual retornando el mensaje 
# "hola <nombre>, tienes <edad> años"


# def mensaje1(nombre:str, a_nac: int, a_actual: int ) -> str:
#     edad = a_actual - a_nac
#     return f"Hola {nombre}, tienes {edad} años"

# def mensaje2(nombre:str, a_nac: int, a_actual: int ) -> str:
#     return f"Hola {nombre}, tienes {a_actual - a_nac} años"

# def calcular_edad(a_nac: int, a_actual: int )->int:
#     return a_actual - a_nac

# def mensaje3(nombre:str, a_nac: int, a_actual: int ) -> str:
#     return f"Hola {nombre}, tienes {calcular_edad(a_nac, a_actual)} años"


# if __name__ == "__main__":
#     print(mensaje1("Alex", 1980,2022))
#     res = mensaje1("brian", 2001,2022)
#     print(res)
#     print(mensaje3("Regina,", 2010,2022))


#listas
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"]

# print(f"Alumnos: {alumnos}")

# for i in range(len(alumnos)):
#     print(f"Alumnos:{alumnos[i]}")

#Index

#tuplas
# alumnos = ("Hugo", "Paco", "Luis", "Lupita")

# print(f"Alumnos: {alumnos}")

# for i in range(len(alumnos)):
#     print(f"Alumnos {i+1}: {alumnos[i]}")

#Sets

# alumnos = {"Hugo", "Paco", "Luis", "Lupita"}
# print(f"Alumnos: {alumnos}")

#diccionarios
# alumnos = {"nombre": "Hugo", "Materia1":10, "Materia2":5}
# print(f"Alumnos: {alumnos}")
# print(f"Alumnos: {alumnos['nombre']}")

# numeros_list = [1,2,3,1,3,2,34,1,12,1,31,12,3,1,3,2,1,2]
# numeros_set ={1,2,3,1,3,2,34,1,12,1,31,12,3,1,3,2,1,2}
# print(numeros_list)
# print(numeros_set)




h= ["Nombre", "Est Dat", "Programacion func", "ingles"]
al = ["Hugo", "Paco", "Luis", "Lupita"]

m1 = [9, 7, 9, 8]
m2 = [10, 8, 7, 9]
m3 = [6, 9, 7, 10]


print(f"{h[0]}{h[1]}{h[2]}{h[3]:>10}")
for i in range(len(al)):
    print(f"{al[i]:^10}{m1[i]:^10}{m2[i]:^10}{m3[i]:^10}")


def reporte(fmt:int):
    print(f"{h[0]:^{fmt}}{h[1]:^{fmt}}{h[2]:^{fmt}}{h[3]:^{fmt}}")
    for i in range(len(al)):
        print(f"{al[i]:*<{fmt}}{m1[i]:^{fmt}}{m2[i]:>{fmt}}{m3[i]:^{fmt}}")

if __name__ == "__main__":
    reporte(15)





    



