
'''#EXERCICIO 1

a = int(input("me diga um numero:  "))
b = int(input("me diga um numero diferente do primerio:  "))

if a > b:
    print(f'{a} é maior que {b}!')
else:
    print(f'{b} é maior que {a}!')

#EXERCICIO 2

a = int(input("me diga o seu ano de nascimento:  "))

idade = 2025 - a

if idade < 16:
    print("voce ainda nao pode votar!")
else:
    print("voce já pode votar!")


#EXERCICIO 3


a = int(input("insira a sua senha:  "))

if a == 1234:
    print('ACESSO PERMITIDO!')

else:
    print('ACESSO NEGADO!')

#EXERCICIO 4

quantidade = int(input("quantas maçãs voce deseja comprar?  "))

if quantidade <= 11:
    valor = quantidade * 0.30
    print(f'o valor total da compra foi de {valor:.2f}')

else:
    valor = quantidade * 0.25
    print(f'o valor total da compra foi de {valor:.2f}')


#EXERCICIO 5

valor1 = int(input('me informe um primeiro valor: '))
valor2 = int(input('me informe um segundo valor: '))
valor3 = int(input('me informe um terceiro valor: '))

if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(f'a sequencia numerica correta é {valor3} < {valor2} < {valor1}')

if valor1 > valor2 and valor1 > valor3 and valor3 > valor2:
    print(f'a sequencia numerica correta é {valor2} < {valor3} < {valor1}')

elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(f'a sequencia numerica correta é {valor3} < {valor1} < {valor2}')

elif valor2 > valor1 and valor2 > valor3 and valor3 > valor1:
    print(f'a sequencia numerica correta é {valor1} < {valor3} < {valor2}')

elif valor3> valor1 and valor3 > valor2 and valor1 > valor2:
    print(f'a sequencia numerica correta é {valor2} < {valor1} < {valor3}')
#EXERCICIO 6
genero = int(input('qual é o seu genero? (digite 1 para feminino e 2 para masculino)  '))
altura = float(input("diga qual é a sua altura: "))

if genero == 1:
    formula = 62.1 * altura - 44.7
    print(f'seu peso ideal é {formula:.2f}')

elif genero == 2:
    formula = 72.7 * altura - 58
    print(f'seu peso ideal é {formula:.2f}')

#EXERCICIO 7

lados = int(input("me diga o numero de lados do poligono: " ))
perimetro =  float(input("me diga o perimetro do poligono: " ))

if lados == 3:
    print('TRIANGULO')

elif lados == 4:
    print('RETANGULO')

elif lados == 5:
    print('PENTAGONO')

#EXERCICIO 8

elif lados < 3:
    print('isso nao e um poligono')

elif lados > 5:
    print('POLIGONO NAO IDENTIFICADO')

resultado = perimetro * lados
print(f'o valor do perimetro é de {resultado}')

#EXERCICIO 9

valor1 = int(input('me informe um primeiro valor: '))
valor2 = int(input('me informe um segundo valor: '))
valor3 = int(input('me informe um terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    print(f'o numero {valor1} é o maior dos tres numeros')

elif valor2 > valor1 and valor2 > valor3:
    print(f'o numero {valor2} é o maior dos tres numeros')

elif valor3 > valor2 and valor3 > valor1:
    print(f'o numero {valor3} é o maior dos tres numeros')



#EXERCICIO 10
lado1 = int(input('insira cada lado do triangulo: '))
lado2 = int(input('segundo lado: '))
lado3 = int(input('terceiro lado: '))

if lado3 == lado1 and lado3 == lado2:
    print('O TRIANGULO É EQUILÁTERO')
elif lado2 == lado1 or lado3 == lado2 or lado1 == lado3:
    print('O TRIANGULO É ISOSCELES')
else:
    print("O TRIANGULO É ESCALENO")

#EXERCICIO 11

angulo1 = int(input('diga o valor do primeiro angulo:  '))
angulo2 = int(input('diga o valor do segundo angulo:  '))
angulo3 = int(input('diga o valor do terceiro angulo:  '))

if angulo3 == 90 or angulo2 == 90 or angulo1 == 90:
    print("TRIANGULO RETANGULO")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("TRIANGULO OBTUSANGULO")
elif angulo1 < 90 or angulo2 < 90 or angulo3 < 90:
    print("TRIANGULO ACUTANGULO")'''














