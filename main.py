from queue import PriorityQueue
import random

from manipulacao import media
#estou importando uma lista de prioridade nativa do python

from util import arrayToString


def main():
    # Crio uma fila de prioridades com base na biblioteca importada
    q = PriorityQueue()
    #leio as atividades do txt
    f = open("auxiliar.txt", "r")

    # Insere as atividades do txt na fila com os títulos e as prioridades geradas aleatoriamente
    for line in f:
        tarefas = line.replace("\n", "").split(',')
        q.put((random.randint(1, 50), tarefas))

    # Mostro as atividades e suas prioridade em ordem das prioridades
    while not q.empty():
        next_item = q.get()
        print(next_item)

    #tempo fictício de execução do total das atividas das filas
    temexec = [random.randint(1, 60), random.randint(1, 50), random.randint(1, 60), random.randint(1, 60)]
    quantum = 5
    #estou mandando os processos, a quantidade de processos, o tempo e o quantum
    media(q, 4, temexec, quantum)


if __name__ == "__main__":
    main()
