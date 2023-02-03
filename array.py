lista = []

lista.append('Item 1')
lista.append('Item 2')
lista.append('Item 3')
lista.append('Item 4')
lista.append('Item 5')

print('> Lista:', lista)
print('> Tamanhho:', len(lista))
print()

print('> Imprimindo na forma de lista:')
for x in lista:
  print(x)

print()
print('> Removendo o Item 2 -> usando pop()')
lista.pop(1)

print('> Lista:', lista)
print('> Tamanhho:', len(lista))

print()
print('> Removendo o Item 5 -> usando remove()')
lista.remove("Item 5")

print('> Lista:', lista)
print('> Tamanhho:', len(lista))
print()
