def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
media = calcular_media(a, b, c)

print(f"A média é {media}")