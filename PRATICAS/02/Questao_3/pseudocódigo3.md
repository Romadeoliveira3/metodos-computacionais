//Atividade Pseudocódigos
//Questão 03)

#um algoritmo para jogar pedra papel e tesoura contra o computador.

Algoritmo JogoPedraPapelTesoura
    var
        jogador, computador: inteiro

    // Gera uma escolha aleatória para o computador (1 - Pedra, 2 - Papel, 3 - Tesoura)
    computador <- gerarNumeroAleatorio(1, 3)

    // Solicita a escolha do jogador (1 - Pedra, 2 - Papel, 3 - Tesoura)
    leia(jogador)

    // Verifica quem ganhou o jogo
    se jogador == computador então
        escreva("Empate!")
    senão se (jogador == 1 e computador == 3) ou (jogador == 2 e computador == 1) ou (jogador == 3 e computador == 2) então
        escreva("Você ganhou!")
    senão
        escreva("Você perdeu!")
FimAlgoritmo
