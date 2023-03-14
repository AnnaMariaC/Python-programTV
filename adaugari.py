def AfisMeniuAdd():
    print(20 * "-")
    print("   a. Populare lista de program tv din fisier")
    print("   b. Adauga program tv")
    print("   c. Modificare program tv")
    print("   e. Exit spre meniul principal")
    return input("Ce vrei(a,b,c,e):")


def AdaugEnd(Ghid):
    Ziua = input("da o zi:")
    Ghid.append(Ziua)
    Ora = input("da ora difuzarii:")
    Ghid.append(Ora)
    Titlu = input("da un titlu:")
    Ghid.append(Titlu)
    Categoria = input("Categoria(film,show,jurnal,sport):")
    Ghid.append(Categoria)
    Descriere = input(" Cuvinte cheie:")
    Ghid.append(Descriere)
    Durata = int(input(" Durata:"))
    Ghid.append(Durata)


def UpDate(Ghid):
    ZiuaNoua = input("da ziua de actualizat:")
    Index = Ghid.index(ZiuaNoua)  # gaseste indexul care corespunde
    Ora = input("da ora noua:")
    Ghid[Index + 1] = Ora
    Titlu = input("da titlu nou:")
    Ghid[Index + 2] = Titlu  # creste cu o unitate indexul
    Categoria = input("da alta categorie: ")
    Ghid[Index + 3] = Categoria
    Descriere = input("da un nou cuvant: ")
    Ghid[Index + 4] = Descriere
    Durata = int(input("da o alta durata: "))
    Ghid[Index + 5] = Durata


def CitireDinFisier(Ghid):
    # NumeFis=input("da numele fisierului de date ")
    # Fis=open(NumeFis,'r')
    Fis = open('p.txt', 'r')
    Programe = Fis.readlines()
    # print (Programe)
    i = 0;
    for linie in Programe:  # eliminam \n
        linie = linie[0:len(linie) - 1]
        # print(linie)
        Programe[i] = linie
        i += 1
    # print(Programe)
    for linie in Programe:  # impartim elementele dupa separtorul ;
        Aux = linie.split(';')
        Ghid.append(Aux[0])
        Ghid.append(Aux[1])
        Ghid.append(Aux[2])
        Ghid.append(Aux[3])
        Ghid.append(Aux[4])
        Ghid.append(int(Aux[5]))
    return Ghid


def adaugare(Ghid):
    Adaug = {'a': CitireDinFisier, 'b': AdaugEnd, 'c': UpDate}
    opt = AfisMeniuAdd()
    while (opt != 'e'):
        if (opt == 'a'):
            Ghid = Adaug[opt](Ghid)
        else:
            Adaug[opt](Ghid)
        print(Ghid)
        opt = AfisMeniuAdd()
    return

