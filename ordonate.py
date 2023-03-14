def AfisDupaFilm(Ghid):
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    Z = 3
    while (Z < len(Ghid)):
        if (Ghid[Z] == "film"):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[Z - 3], Ghid[Z - 2], Ghid[Z - 1], Ghid[Z], Ghid[Z + 1], Ghid[Z + 2]))
        Z += 6

    print(145 * "=")


def AfisDupaJurnal(Ghid):
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    Z = 3
    while (Z < len(Ghid)):
        if (Ghid[Z] == "jurnal"):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[Z - 3], Ghid[Z - 2], Ghid[Z - 1], Ghid[Z], Ghid[Z + 1], Ghid[Z + 2]))
        Z += 6

    print(145 * "=")


def AfisDupaShow(Ghid):
    print(145 * "=")
    print("|Ziua", 9 * " ", "|Ora", 10 * " ", "|Titlu", 32 * " ", "|Categoria", 12 * " ", "|Descriere ", 27 * " ",
          "|Durata\t|")
    print(145 * "-")
    Z = 3
    while (Z < len(Ghid)):
        if (Ghid[Z] == "show"):
            print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (
            Ghid[Z - 3], Ghid[Z - 2], Ghid[Z - 1], Ghid[Z], Ghid[Z + 1], Ghid[Z + 2]))
        Z += 6

    print(145 * "=")


def AfisMeniuOrdo():
    print(20 * "-")
    print("   a. Afiseaza toate filmele")
    print("   b. Afiseaza toate jurnalele")
    print("   c. Afiseaza toate show-urile")
    print("   e. Exit spre meniul principal")
    return input("Ce vrei(a,b,c,e):")


def ordonate(Ghid):
    Caut = {'a': AfisDupaFilm, 'b': AfisDupaJurnal, 'c': AfisDupaShow}
    opt = AfisMeniuOrdo()
    while (opt != 'e'):
        Caut[opt](Ghid)
        opt = AfisMeniuOrdo()
    return


