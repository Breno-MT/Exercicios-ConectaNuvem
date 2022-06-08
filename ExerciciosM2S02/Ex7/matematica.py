def somar(a,b):
    print("-*-"*6)
    return a + b

def multiplicar(a,b):
    print("-*-"*6)
    return a * b

def subtrair(a,b):

    print("-*-"*6)
    return a - b

def divisao(a,b):
    print("-*-"*6)
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Não tente dividir por 0! {e}")
    except:
        print("Tente novamente.")
    print("-*-"*6)
