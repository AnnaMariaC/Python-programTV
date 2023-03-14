from adaugari import *
from stergeri import *
from ordonate import *
from saptamana import *
from descrescator import *




def SalvFis(Ghid):
    NumeFis=input("da numele fisierului in care salvezi:")
    Fis=open(NumeFis,"w")
    i=0
    while(i<len(Ghid)):
        sir=""
        sir = sir + str(Ghid[i]) + ";" + str(Ghid[i + 1]) + ";" + str(Ghid[i + 2]) + ";" + str(Ghid[i + 3]) + str(Ghid[i + 4])+ ";" + str(Ghid[i + 5]) + "\n"
        Fis.write(str(sir))

    i+=6
    Fis.close()


def afisare(Ghid):
    print(Ghid)
    print(145*"=")
    print("|Ziua",9*" ","|Ora", 10*" ","|Titlu",32*" ","|Categoria", 12*" ","|Descriere ", 27*" ","|Durata\t|" )
    print(145*"-")
    Index=0
    while(Index<len(Ghid)-5):
         print("|%8s\t|%-8s\t|%-36s\t|%-18s\t|%-35s\t|%d\t|" % (Ghid[Index],Ghid[Index+1],Ghid[Index+2],Ghid[Index+3],Ghid[Index+4],Ghid[Index+5])  )     #tiparire cu format
         Index+=6
    print(145*"=")

def AfisMeniu():
    print(30*'=')
    print("1.Adaugare program tv")
    print("2.Stergere program tv")
    print("3.Afisare dupa o categorie")
    print("4.Afisare ordonata descrescator")
    print("5.Program tv pe o zi saptamana")
    print("6.Afisare program tv in forma bruta")
    print("7.Salvare in fisier")
    print("0.Terminare Program")
    print(30*'=')
    return int(input("Ce Vrei(1,2,3,4,5,6,7,0):"))

def Main():
    Ghid=[]
    Funct={1:adaugare,2:stergere,3:ordonate,4:descrescator,5:saptamana,6:afisare,7:SalvFis}
    while(True):
        Opt=AfisMeniu()
        if(Opt==0):
            break
        Funct[Opt](Ghid)
    print("Program terminat")
Main()

