km = int(input('A quantos km/h voce esta dirigindo?'))
if (km < 100):
    print('Parabéns você estpa abaixo do limite')
elif(km > 100):
    print('Você ganhou multa, está acima do limite!')
else:
    print('Você está no limite de velocidade')