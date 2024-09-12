print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("alguien usó la función hola")

def chat(mensa):
    print(f"Chat {mensa}")
def ellacontesta(mensa):
    print(f"chat ella {mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")
def suma(a,b):
    s=a+b
    return s
def resta(c,d):
    r=c-d
    return r
def multiplicacion(e,f):
    m=e*f
    return m
def division(g,h):
    d=g/h
    return d

# llamada a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Pereyra","Ever")
print("Operacion suma")
c1 = int(input("ingresa un numero "))
c2 = int(input("ingresa un numero "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")
print("Operacion resta")
c3 = int(input("ingresa un numero "))
c4 = int(input("ingresa un numero "))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")
print("Operacion multiplicacion")
c5 = int(input("ingresa un numero "))
c6 = int(input("ingresa un numero "))
damemultiplicacion=multiplicacion(c5,c6)
print(f"La multiplicacion de {c1} X {c2} = {damemultiplicacion}")
print("Operacion division")
c7 = int(input("ingresa un numero "))
c8 = int(input("ingresa un numero "))
damedivision=division(c7,c8)
print(f"La division de {c7} + {c8} = {damedivision}")


