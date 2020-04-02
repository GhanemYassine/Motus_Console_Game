from random import *

n=0
kelma=""
tabda='a'
momken=[]
occ=[0]*30

def Saisie():
    f=open("Dico.txt","r")
    global momken
    global n
    global tabda
    global kelma
    global occ
    n=int(input("Nombre de lettres (entre 7 et 10)"))
    tabda=chr(ord('a')+randint(0,26))
    for i in f:
        i=i.rstrip(" \n")
        if len(i)==n and i[0]==tabda:
            momken.append(i)
    kelma=choice(momken)
    print (kelma)
    for i in kelma:
        occ[ord(i)-ord('a')]=occ[ord(i)-ord('a')]+1

def Khedma(multi):
    attempts=1
    print("Vous cherchez un mot de " + str(n) + " mots, Vous avez 6 essais")
    print(kelma[0].upper(),end="")
    for i in range(n-1):
        print(".",end="")
    print()        
    while attempts<=6 :
        print("PLAYER 1 turn ")
        print(attempts,end=" ")
        
        het=input()
        ans=['.']*n
        taw=[0]*26
        if het[0]!=tabda:
            print("Première lettre non valide")
        elif len(het)!=n:
            print("Longueur non valide")
        elif het not in momken:
            print("Pas dans le dictionnaire")
        else:
            shih=0
            for i in range(n):
                if het[i]==kelma[i]:
                    ans[i]=kelma[i].upper()
                    shih=shih+1
                    
            if shih==n:
                print ("Felicitations Player 1!")
                break
            for i in range(n):
                if het[i]!=kelma[i] and taw[ord(het[i])-ord('a')]<occ[ord(het[i])-ord('a')]:
                    ans[i]=het[i]
                taw[ord(kelma[i])-ord('a')]=taw[ord(kelma[i])-ord('a')]+1
            print("".join(ans))
        ans=['.']*n
        taw=[0]*26
        print("Player 2 turn : ")
        print(attempts,end=" ")
        if (multi==1):
            het=choice(momken)
        else:
            het=input()
        if het[0]!=tabda:
           print("Première lettre non valide")
        elif len(het)!=n:
            print("Longueur non valide")
        elif het not in momken:
            print("Pas dans le dictionnaire")
        else:
            shih=0
            for i in range(n):
                if het[i]==kelma[i]:
                    ans[i]=kelma[i].upper()
                    shih=shih+1
                    
            if shih==n:
                print ("Felicitations Player 2!")
                break
            for i in range(n):
                if het[i]!=kelma[i] and taw[ord(het[i])-ord('a')]<occ[ord(het[i])-ord('a')]:
                    ans[i]=het[i]
                taw[ord(kelma[i])-ord('a')]=taw[ord(kelma[i])-ord('a')]+1
            print("".join(ans))
        attempts=attempts+1


multi=int(input("(1)Solo\n(2)Multi\n"))
Saisie()
Khedma(multi)







        
