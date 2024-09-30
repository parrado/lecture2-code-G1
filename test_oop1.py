from math import pi

# Define clase Circulo con 3 atributos
class Circulo:
    # Función constructor, se llama cuando se crea el objeto
    # El constructor define 3 atributos
    def __init__(self,radio,centroX,centroY):
        self.radio=radio
        self.centroX=centroX
        self.centroY=centroY

    # Se definen dos métodos para la clase Circulo
    def area(self):
        return pi*self.radio**2
    
    def perimetro(self):
        return 2*pi*self.radio

# Crea dos objetos (2 instancias) de la clase Circulo
myCircle0=Circulo(1.0,0.0,0.0)
myCircle1=Circulo(2.0,-0.1,0.1)

# Invoca métodos de la clase Circulo desde el objecto myCircle0
a=myCircle0.area()
p=myCircle0.perimetro()

print(f'El área es: {a} y el perímetro es: {p}')

# Invoca métodos de la clase Circulo desde el objecto myCircle1
a=myCircle1.area()
p=myCircle1.perimetro()

print(f'El área es: {a} y el perímetro es: {p}')


# Imprime las referencias de los objetos tipo Circulo
print(myCircle0)
print(myCircle1)

print(type(myCircle0))
print(type(3.141592654)) 

# Imprime la clase Circulo
print(Circulo)        