#Funcion de Potencia 
def Potencia():
    res=1
    print("Ingrese el numero a potenciar")
    num1=int(input())
    print("Ingrese el exponente")
    exponente=int(input())

    for i in range(0,exponente):
        res=res*num1
    
    print("El resultado de",num1,"elevado a la",exponente,"es",res)

Potencia()