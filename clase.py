def sumar(a:int|float, b:int|float) -> int|float:
    return a+b

def restar(a:int|float, b:int|float)->int|float:
    return a-b

def dividir(a:int|float, b:int|float)->int|float:
    return a/b

def multiplicar(a:int|float, b:int|float)->int|float:
    return a*b

def cuadrado(a:int|float, b:int|float)->int|float:
    return a*a


if __name__ == "__main__":
    print(sumar(5,6))
    print(restar(5,6))
    print(multiplicar(5,6))