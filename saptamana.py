def SortezDupaOra(Ghid):
    flag = True
    while (flag):
        flag = False
        i = 0
        while (i < len(Ghid) - 11):
            if (Ghid[i + 1] > Ghid[i + 7]):
                aux = Ghid[i]
                Ghid[i] = Ghid[i + 6]
                Ghid[i + 6] = aux
                aux1 = Ghid[i + 1]
                Ghid[i + 1] = Ghid[i + 7]
                Ghid[i + 7] = aux1
                aux2 = Ghid[i + 2]
                Ghid[i + 2] = Ghid[i + 8]
                Ghid[i + 8] = aux2
                aux3 = Ghid[i + 3]
                Ghid[i + 3] = Ghid[i + 9]
                Ghid[i + 9] = aux3
                aux4 = Ghid[i + 4]
                Ghid[i + 4] = Ghid[i + 10]
                Ghid[i + 10] = aux4
                aux5 = Ghid[i + 5]
                Ghid[i + 5] = Ghid[i + 11]
                Ghid[i + 11] = aux5
                flag = True
            i += 6


def AfisDupaZi(Ghid):
    Ziua = input("Da o zi de afisat: ")
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    SortezDupaOra(Ghid)
    I = 0
    while (I < len(Ghid) - 5):
        if (Ghid[I] == Ziua):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[I], Ghid[I + 1], Ghid[I + 2], Ghid[I + 3], Ghid[I + 4], Ghid[I + 5]))
        I += 6

    print(145 * "=")


def AfisMeniuCaut():
    print(20 * "-")
    print("   a. Afiseaza programul tv dintr-o zi")
    print("   e. Exit spre meniul principal")
    return input("Ce vrei(a,e):")


def saptamana(Ghid):
    Caut = {'a': AfisDupaZi}
    opt = AfisMeniuCaut()
    while (opt != 'e'):
        Caut[opt](Ghid)
        opt = AfisMeniuCaut()
    return
