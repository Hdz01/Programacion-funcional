def mensaje(msg: str, nombre: str):
    print(msg, nombre)

def mensaje_edad(nombre: str, edad: int): 
    print("Hola", nombre, "Tienes", edad, "Años")

def calcular_edad(a_actual: int, a_nacimiento: int)-> int:
    return a_actual - a_nacimiento

if __name__ == "__main__":
    mensaje("Buenos dias", "Alex")
    mensaje_edad("Alex", 50)
    mensaje_edad("Alexander", calcular_edad(2022,1969))
