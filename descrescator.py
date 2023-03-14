def SortezDupaDurata(Ghid):
    flag = True
    while (flag):
        flag = False
        i = 0
        while (i < len(Ghid) - 11):
            if (Ghid[i + 5] < Ghid[i + 11]):
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


def AfisSport(Ghid):
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    SortezDupaDurata(Ghid)
    Z = 3
    while (Z < len(Ghid)):
        if (Ghid[Z] == "sport"):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[Z - 3], Ghid[Z - 2], Ghid[Z - 1], Ghid[Z], Ghid[Z + 1], Ghid[Z + 2]))
        Z += 6

    print(145 * "=")


def AfisJurnal(Ghid):
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    SortezDupaDurata(Ghid)
    Z = 3
    while (Z < len(Ghid)):
        if (Ghid[Z] == "jurnal"):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[Z - 3], Ghid[Z - 2], Ghid[Z - 1], Ghid[Z], Ghid[Z + 1], Ghid[Z + 2]))
        Z += 6

    print(145 * "=")


def AfisMeniuDesc():
    print(20 * "-")
    print("   a. Afiseaza stirile sportive descrescator dupa durata")
    print("   b. Afiseaza jurnalul descrescator dupa durata")
    print("   e. Exit spre meniul principal")
    return input("Ce vrei(a,b,e):")


def descrescator(Ghid):
    Caut = {'a': AfisSport, 'b': AfisJurnal}

    opt = AfisMeniuDesc()

    while (opt != 'e'):
        Caut[opt](Ghid)
        opt = AfisMeniuDesc()
    return
