termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Agora digite a razão da PA: '))


decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end=' => ')
print('ACABOU!')
