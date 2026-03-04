n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maiorNumero = n1
menorNumero = n1

if n2 > maiorNumero:
    maiorNumero = n2
if n3 > maiorNumero:
    maiorNumero = n3

if n2 < menorNumero:
    menorNumero = n2
if n3 < menorNumero:
    menorNumero = n3

print(f'O maior número é: {maiorNumero}')   
print(f'O menor número é: {menorNumero}')