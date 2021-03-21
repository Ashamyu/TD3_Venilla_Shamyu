#!/usr/bin/env python

def mul_num(a,b):
        sum que deux=a+b;
        return sum;

def main():
        import sys
        print(sys.argv)
        i=(len(sys.argv)-1)
        print("Le nombre d'arguments : ",i)



        if (i==2):
               x = int (sys.argv[1])
               y = int (sys.argv[2])
               print(mul_num(x,y))
        else:
               print("Erreur : Veuillez inserer que deux arguments")

main()
