class Ejemplo:
    #atributos
    valor1=10
    valor2=5
    #métodos
    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es: ", suma)

    def multiplicar(self):
       multi = self.valor1 * self.valor2
       print ("la multiplicacion es: ", multi)

    def promediar(self):
        prom = (self.valor1 + self.valor2)/2
        print ("El promedio es: ", prom)
