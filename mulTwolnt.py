#!/usr/bin/env python

def mul_num(a,b):
        sum=a+b;
        return sum;

def main():
        import sys
        print(sys.argv)
        i=(len(sys.argv)-1)
        print("Le nombre d'arguments : ",i)


        if (i==0):
               n1=int(input("Inserez le premier argument : "))
               n2=int(input("Inserez le deuxieme argument : "))
               x = int (n1)
               y = int (n2)
               print(mul_num(x,y))
        elif (i==1):
               n1=int(input("Inserez le deuxieme argument : "))
               x = int (sys.argv[1])
               y = int (n1)
               print(mul_num(x,y))
        elif (i==2:
               x = int (sys.argv[1])
               y = int (sys.argv[2])
               print(mul_num(x,y))
        else:
               print("Erreur : Veuillez inserer que deux arguments")

main()
                
