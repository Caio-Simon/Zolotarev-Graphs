import pydot

def main():
    n=int(input("Give the n of Z(n,L): "))
    L=int(input("Now give the L of Z(n,L): "))
    n=n%L
    Ln,g=LN(n,L)
    print("Ln = ", Ln)
    print("gcd(n,L) = ", g)
    b=L/Ln
    i=0
    Z="digraph {\n"
    while i<L:
        j=(i*n)%L
        if i%g!=0:#leaf
            Z=Z+str(i)+"""[color="darkgreen"];\n"""+str(i)+"->"+str(j)+";\n"
        elif i%b!=0:#branch
            Z=Z+str(i)+"""[color="chocolate4"];\n"""+str(i)+"->"+str(j)+";\n"
        else:#root
            Z=Z+str(i)+"""[color="red"];\n"""+str(i)+"->"+str(j)+"[constraint=false];\n"
        i+=1
    Z=Z+"}"
    graphs = pydot.graph_from_dot_data(Z)
    graph = graphs[0]
    graph.write_png("Z("+str(n)+","+str(L)+").png")
    if input("If you want to calculate more graphs press some buttom and give enter, if not just give enter: ")=="":
        return
    else:
        main()
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def LN(n,L):
    k=gcd(L,n)
    Ln1=L
    Ln=Ln1/k
    while Ln!=Ln1:
        Ln1=Ln
        Ln=Ln1/gcd(Ln1,n)
    return Ln,k
main()