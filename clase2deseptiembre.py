#reporte de calificaciones

# h= ["Nombre", "Est Dat", "Programacion func", "ingles"]
# al = ["Hugo", "Paco", "Luis", "Lupita"]

# m1 = [9, 7, 9, 8]
# m2 = [10, 8, 7, 9]
# m3 = [6, 9, 7, 10]


# print(f"{h[0]}{h[1]}{h[2]}{h[3]:>10}")
# for i in range(len(al)):
#     print(f"{al[i]:^10}{m1[i]:^10}{m2[i]:^10}{m3[i]:^10}")


# def reporte(fmt:int):
#     print(f"{h[0]:^{fmt}}{h[1]:^{fmt}}{h[2]:^{fmt}}{h[3]:^{fmt}}")
#     for i in range(len(al)):
#         print(f"{al[i]:*<{fmt}}{m1[i]:^{fmt}}{m2[i]:>{fmt}}{m3[i]:^{fmt}}")

# if __name__ == "__main__":
#     reporte(15)



# #separacion con comas
# numbig = 12837182937912379124712847281471284142
# print(f"{numbig:,d}")

# #fijar cantidad por decimales
# numPi = 3.1416762987583272347274127124430
# print(f"{numPi:.3f}")

# #por exponencial
# print(f"{numPi:e}")

# #exponencial con pocas decimas
# print(f"{numPi:.2e}")

# #porcentaje
# numeroporciento = 0.258478585
# print(f"{numeroporciento: %}")
# print(f"{numeroporciento: .2%}")

#Numeros binarios
# print(f"{25*5:b}")

# #unicodes
# print(f"{98:c}")

# #hexadecimal
# print(f"{255:x}")

# #octal
# print(f"{255:o}")


def producto(a:int,b=int)->int: return a*b

def tablas(m: int, n: int, fmt: int):
    for i in range(1, m+1):
        tabla(n,i,fmt)

def tabla(n:int, t:int, fmt: int):
    for i in range (1,n+1):
        print (f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")

if __name__ == "__main__":
    tablas(9,4,4)