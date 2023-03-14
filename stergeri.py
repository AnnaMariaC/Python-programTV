def AfisMeniuAdd():
    print(20*"-")
    print("   a. Stergere dupa zi")
    print("   b. Stergere dupa titlu")
    print("   e. Exit spre meniul principal")
    print(20*"-")
    return input("Ce vrei(a,b,e):")

def DupaZi(Ghid):
    Ziua=input('Da ziua de sters:')
    G=0
    while(G<len(Ghid) and Ghid[G]!=Ziua):
        G+=6
    if(G>=len(Ghid)): print('n-am gasit ziua cautata!!!')
    else:
        Index=0
        while(Index<6):
            Ghid.remove(Ghid[G])
            Index+=1
        print('s-a sters ziua ceruta. verifica prin afisare')

def DupaTitlu(Ghid):
    Titlu=input('Da titlu  de sters:')
    G=2
    while(G<len(Ghid) and Ghid[G]!=Titlu):
        G+=6
    if(G>len(Ghid)): print('nu-am gasit titlu  cerute!!!')
    else:
        Index=0
        while(Index<6):
            Ghid.remove(Ghid[G-2])
            Index+=1
        print('s-a sters titlul  ceruta. verifica prin afisare')



def stergere(Ghid):
    Sterg={'a':DupaZi,'b':DupaTitlu}
    opt=AfisMeniuAdd()
    while(opt!='e'):
        Sterg[opt](Ghid)
        opt=AfisMeniuAdd()
