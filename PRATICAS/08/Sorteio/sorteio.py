import random

def sorteio(nomes, n, nome_sorteado):
    """
    Sorteia o vencedor de um prêmio de acordo com as regras fornecidas.

    Args:
      nomes: Uma lista de nomes dos concorrentes.
      n: Um número inteiro positivo que determina o número de pessoas a serem eliminadas a cada rodada.
      nome_sorteado: O nome do concorrente sorteado para iniciar a contagem.

    Returns:
      O nome do vencedor do prêmio.
    """

    # Iniciar com o concorrente sorteado
    contador = nomes.index(nome_sorteado)
    # Execute até restar apenas um concorrente;
    while len(nomes) > 1:
        # Calcule o próximo índice a ser removido
        contador = (contador + n) % len(nomes)
        # Remova e mostre o concorrente eliminado
        nome_atual = nomes.pop(contador)
        print(f'{nome_atual} foi eliminado.')
    # Ultimo concorrente é o vencedor
    vencedor = nomes[0]

    return vencedor

if __name__ == "__main__":
    # Lista de nomes dos concorrentes.
    nomes = ["Luiz", "Fernanda", "Amanda", "Ricardo", "José", "Flávia", "Lucas", "Roberta", "Pedro", "Júlia"]

    # Sorteia o nome do concorrente que inicia a contagem.
    nome_sorteado = random.choice(nomes)
    print(f'O concorrente sorteado inicialmente é: {nome_sorteado}')

    # Sorteia o vencedor do prêmio.
    vencedor = sorteio(nomes, 3, nome_sorteado)

    # Imprime o nome do vencedor.
    print(f'\nA pessoa que venceu o grande prêmio é: {vencedor}')
