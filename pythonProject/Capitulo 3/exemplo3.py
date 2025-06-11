def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

n1 =  int(input("digite um numero inteiro: "))
n2 =  int(input("digite um numero inteiro: "))


resultadoSoma = soma(n1, n2)
resultadoSubtracao = subtracao(n1,n2)
resultadoMultiplicacao = multiplicacao(n1,n2)

print(f"O resultado da função soma é: {resultadoSoma} o resultado da subtracao é {resultadoSubtracao} o resultado da multiplicacao é: {resultadoMultiplicacao}")