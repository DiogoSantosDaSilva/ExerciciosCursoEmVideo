from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('\033[35m=\033[m'*34)
print()
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

