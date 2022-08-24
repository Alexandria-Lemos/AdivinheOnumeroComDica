from random import randint
pc = randint(0, 10)
socorro = '\033[35mSOCORRO\033[m'
print('\033[1;35m<==========ADIVINHE O NÚMERO==========>')
print('\033[1;33mSOCORRO, pensou em um número de 0 a 10...Adivinhe qual!\033[m')
print('\033[34m=+==+=\033[m' * 10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('O Número é? '))
    cont += 1
    print('\033[34m=+==+=\033[m' * 10)
    if jogador != pc:
        print('\033[36mERROU!... ( U´3U)\033[m')
        print('\033[31m//////\033[m' * 10)
    if jogador == pc:
        acertou = True
        print('\033[36mPARABENS, você ACERTOU.....(-´,´-)!\033[m')
        print('{} pensou em {}, você chutou {}...'.format(socorro, pc, jogador))
        print('\033[35m====================+Foram {} temtativas+====================\033[m'.format(cont))
    else:
        if jogador < pc:
            print('Tente um Maior...')
        else:
            print('Tente um Menor...')