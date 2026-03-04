numeroSecreto = 49
num = 0
while num != numeroSecreto:
    num = int(input('Digite seu palpite:'))
    if num < numeroSecreto:
        print('o numero secreto é mais alto')
    else:
        print('o numero secreto é menor')
print(f'Parabens o numero secreto é: {numeroSecreto}')