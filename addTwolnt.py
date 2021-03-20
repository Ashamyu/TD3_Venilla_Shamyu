
def add(a,b):
    sum=a+b;
    return sum;

def main():
    import sys
    print(sys.argv)
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    print (add(x,y))
main()
