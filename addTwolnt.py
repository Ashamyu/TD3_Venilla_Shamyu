
def add(a,b):
    sum=a+b;
    return sum;

def main():
    import sys
    print(sys.argv)
    i=(len(sys.argv)-1)
    print("le nombre d'arguments : ",i)

    if (i==2):
           x=int(sys.argv[1])
           y=int(sys.argv[2])
           print (add(x,y))
    else:
           print("erreur : veuiller inserez que deux arguments")
main()
