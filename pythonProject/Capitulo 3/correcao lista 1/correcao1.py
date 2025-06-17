
def soma (n1,n2):
    return n1+n2


def subtracao(n1,n2):
    return (n1-n2)

def multiplicacao(n1,n2):
    return(n1*n2)

def divisao(n1,n2):
    return(n1/n2)

n1  = int(input('digite o primeiro numero: '))
n2 = int(input('digite outro numero'))
resultadoSoma = soma(n1,n2)
resultadoSub = subtracao(n1,n2)
resultadoMulti = multiplicacao(n1,n2)
resultadoDivi = divisao(n1,n2)


print(f' o resultado da soma entre os numeros é de: {resultadoSoma}, resultado divisao{resultadoDivi}, resultado subtracao é {resultadoSub}, resultado da multiplicacao é: {resultadoMulti}')

