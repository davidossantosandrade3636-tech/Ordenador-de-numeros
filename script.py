lista=[]
while True:
    num=int(input('digite um valor:'))
    if num in lista:
     print('numero duplicado não adicionado')

    if num not in lista:
       lista.append(num)
       print('numero adicionado com sucesso')
    resp=input('deseja continuar?[s/n]')

if resp=='n':
        break
lista.sort()
print(f'os numeros foram {lista}')
