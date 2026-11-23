# Абстракция

class Calculator:

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

calculato = Calculator()
print()
print(calculato.multiply(5,3))
print(calculato.divide(10,2))