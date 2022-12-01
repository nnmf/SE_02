# Aqui eu encontra o tempo de espera de todos os processos
def tempodeespera(processos, n, te, wt, quantum):
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = te[i]

    t = 0

    while 1:
        sair = True

        for i in range(n):
            if rem_bt[i] > 0:
                sair = False  # Processo pendente

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum

                else:
                    t = t + rem_bt[i]
                    wt[i] = t - te[i]
                    rem_bt[i] = 0

        if sair == True:
            break


# Calcula o tempo de turn around
def tempoturnaround(processos, n, te, wt, tat):
    for i in range(n):
        tat[i] = te[i] + wt[i]


# Calculo a média dos tempos de
def media(processos, n, te, quantum):
    wt = [0] * n
    tat = [0] * n

    tempodeespera(processos, n, te, wt, quantum)

    tempoturnaround(processos, n, te, wt, tat)

    #mostro os tempos de processos
    print("Processos\t\tTempo de Execucao\t\tTempo de Espera\t\tTempo de turnaround")
    tempoDeEsperaTotal = 0
    taTotal = 0
    for i in range(n):
        tempoDeEsperaTotal = tempoDeEsperaTotal + wt[i]
        taTotal = taTotal + tat[i]
        print(" ", i + 1, "\t\t\t\t", te[i], "\t\t\t\t\t", wt[i], "\t\t\t\t", tat[i])

    #mostro as médias
    print("\nTempo de espera médio: %.5f " % (tempoDeEsperaTotal / n))
    print("Tempo de turnaround médio: %.5f " % (taTotal / n))
