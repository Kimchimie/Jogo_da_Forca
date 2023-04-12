#Jogo da Forca em Python
#Desenvolvedor: Kimie
#Versão: 1.0

#Menu de Boas Vindas
print("********************************")
print("***Bem vindo ao jogo da forca***")
print("********************************")

palavra_secreta = "nictofobia".upper()
letras_acertadas = ["_" for letra in palavra_secreta]

print( letras_acertadas )

#Variaveis de validação e verificação do jogo
enforcou = False
acertou = False
erros = 0

#controle de fim de jogo "Enquanto"
while( not enforcou and not acertou ):
    chute = input( "Qual a letra? " )
    chute = chute.strip().upper()

    if( chute in palavra_secreta ):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1

    print(letras_acertadas)
    print('Chutes errados', erros)

    if ( erros == 10 ):
        enforcou = True

    if( "_" not in letras_acertadas):
        acertou = True

if( acertou == True):
    print("Você ganhou!!")
    print("Parabéns pela sua vitória;D")

if( enforcou == True):
    print("Você perdeu!!")
    print("Fim de jogo, boa sorte na próxima^^")

    input()