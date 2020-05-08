''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        Gpower = list(map(int,input().split()))
        Gpower.sort(reverse=True)
        Opower = list(map(int,input().split()))
        Opower.sort(reverse=True)
        k=0
        l=[]
        c=0
        for i in range(n):
            for j in range(c,n):
                if(Gpower[i] > Opower[j]):
                    c = j+1
                    k+=1
                    break
        print(k)

main()
