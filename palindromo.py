frase=input("digite uma palavra ou frase:")
limpa=frase.lower().replace(" ","")
print(limpa)
invertida=limpa[::-1]

if limpa == invertida:
    print('É um palindromo')

else:
    print('Não é um palindromo')
