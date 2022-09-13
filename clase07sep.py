# lista1 = [1,2,3,4]
# print(lista1)
# lista2 = [1,3.14,"a",True, [4,5,6], (1,2,3),{8,"a",5.4}]
# print(lista2)

# print(len(lista1))
# print(len(lista2))
# print(lista2[6])

# lista_cal = []
# print(lista_cal)
# lista_cal.append(5)
# print(lista_cal)
# lista_cal.append(8)
# print(lista_cal)

# #rellenar una lista con numeros naturales del 1 al 10
# listanat=[]
# for i in range (1,11):
#     listanat.append(i)
# print(listanat)

# #Indices negativos 
# print(lista1[-4])

# #slices (rebanadas)
# lista1 = [1,2,3,4,5,6,7,8,9,10]
# print(lista1)
# print(lista1[:])
# print(lista1[0:10])
# print(lista1[int(len(lista1)/2):])

# print(lista1[:int(len(lista1)/2)])
# print(lista1[0:-1])
# print(lista1[3:7])
# print(lista1[-7:-3])


# lista1 = [1, "dos", 3, "cuatro"]
# # print(lista1)
# # lista1[1] = 2
# lista2 = lista1
# print(f"lista1: {lista1}")
# print(f"lista2: {lista2}")
# lista2[1] = 2
# print("--------------")
# print(f"direccion:lista1 {id(lista1)}lista1:{lista1}")
# print(f"direccion:lista2 {id(lista2)}lista2:{lista2}")
# print("forma correcta")
# lista1 = [1, "dos", 3, "cuatro"]
# lista2 = lista1 [:]
# print(f"direccion:lista1 {id(lista1)}")
# print(f"direccion:lista2 {id(lista2)}")
# lista2[1] = 2
# lista2[3] = 4
# print(f"direccion:lista1 {id(lista1)}lista1:{lista1}")
# print(f"direccion:lista2 {id(lista2)}lista2:{lista2}")


lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
# lista1[5:] =  [5,6,7]
# print(lista1)

# lista1[len(lista1):] = lista2
# print(lista1)
#insertar al inicio de la lista varios elementos (en una lista)
# lista1[:0] = lista2
# print(lista1)


lista1.extend(lista2)
# lista1.append(lista2)
print(lista1)

del lista1[0]
print(lista1)

del(lista1[2:5])
print(lista1)