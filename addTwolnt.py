
def add(a,b):
    sum=a+b;
    return sum;

def main():
    import sys
    print(sys.argv)
    i=(len(sys.argv)-1)
    print("le nombre d'arguments : ",i)

    if (i==0):
           ar1=int(input("Inserez le premier argument : "))
           ar2=int(input("Inserez le deuzieme argument : "))
           x=int(ar1)
           y=int(ar2)
           print (add(x,y))
    elif(i==1):
           ar1=int(input("Inserez le deuzieme argument : "))
           x=int(sys.argv[1])
           y=int(ar1)
           print (add(x,y))
    elif(i==2):
           x=int(sys.argv[1])
           x=int(sys.argv[2])
           print (add(x,y))
    else:
           print("erreur : veuiller inserez que deux arguments")
main()
